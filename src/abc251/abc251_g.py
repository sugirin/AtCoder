"""
https://atcoder.jp/contests/abc251/tasks/abc251_g
"""

import math
import bisect
from heapq import (
    heapify, 
    heappush as hpush,
    heappop as hpop,
)
from typing import List, Tuple

def main():
    pass
    # N = int(input())
    # N, M = map(int, input().split())
    # S = input()
    # T = input().split()
    # A = list(map(int, input().split()))
    # queries = [map(int,input().split()) for _ in range(N)]


# =======================================================
#                       Utilities
# =======================================================
def sieve_of_eratosthenes(N: int) -> List[bool]:
    """エラトステネスの篩。

    Args:
        N (int): 判定する整数の最大値

    Returns:
        List[bool]: 長さN+1の配列で、nが素数ならList[n] = True (2<=n<=N)
                    また、List[0] = List[1] = False
    
    Doctest:
        >>> sieve_of_eratosthenes(10)
        [False, False, True, True, False, True, False, True, False, False, False]
        >>> len(sieve_of_eratosthenes(100))
        101
        >>> sieve_of_eratosthenes(100)[89]
        True
        >>> sieve_of_eratosthenes(100)[57]
        False
    """
    primes = [True for i in range(N+1)]
    primes[0] = False
    primes[1] = False

    sqrt_n = math.ceil(math.sqrt(N))
    for i in range(2, sqrt_n):
        if primes[i]:
            for j in range(2*i, N+1, i):
                primes[j] = False
    return primes

def factorization(x: int) -> List[Tuple[int, int]]:
    """素因数分解

    Args:
        x (int): 素因数分解する整数

    Returns:
        List[Tuple[int, int]]: x = p1^q1 * p2^q2 * ... の時、 [(p1, q1), (p2, q2), ...] のlist
    
    Doctest:
        >>> factorization(24)
        [(2, 3), (3, 1)]
        >>> factorization(360)
        [(2, 3), (3, 2), (5, 1)]
        >>> import math
        >>> math.prod([p**q for p, q in factorization(1234567890)])
        1234567890
    """
    assert x>0
    factor = []
    for i in range(2, x):
        if i*i > x:
            break
        if x % i == 0:
            cnt = 0
            while x % i == 0:
                cnt += 1
                x //= i
            factor.append((i, cnt))
    
    # sqrt(n)まで試し割りして割り切れなかった時
    if x != 1:
        factor.append((x, 1))

    return factor

class BIT:
    """Binary Indexing Tree
    OrderBITクラスから使われることを想定しているので、これを直接使うことは少ない
    """

    def __init__(self,len_A):
        self.N = len_A + 10
        self.bit = [0]*(len_A+10)
        
    # sum(A0 ~ Ai)
    # O(log N)
    def query(self,i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            idx -= idx&(-idx)
        return res

    # Ai += x
    # O(log N)
    def update(self,i,x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx&(-idx)
    
    # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
    # O(log N)
    def lower_left(self,w):
        if (w < 0):
            return -1
        x = 0
        k = 1<<(self.N.bit_length()-1)
        while k > 0:
            if x+k < self.N and self.bit[x+k] < w:
                w -= self.bit[x+k]
                x += k
            k //= 2
        return x

class OrderBIT:
    """順序付き集合
    最初に、集合の元の全候補のリスト(all_values)を与えてこのクラスのインスタンスを作る。
    all_valuesがすでにソートされている場合はsort_flag=Trueにする。
    Interfaces:
        self.insert(x: Any, c=1: Int)
        self.erase(x: Any, c=1: Int)
        self.count_lower(x: Any) -> Int
        self[k: Int] -> Any
    """
    
    def __init__(self, all_values, sort_flag=False):
        if sort_flag:
            self.A = all_values
        else:
            self.A = sorted(all_values)
        self.B = BIT(len(all_values))
        self.num = 0
        
    def insert(self, x, c=1):
        k = bisect.bisect_left(self.A, x)
        self.B.update(k, c)
        self.num += c
    
    def erase(self, x, c=1):
        self.insert(x, -c)
    
    # count the number of values lower than or equal to x
    def count_lower(self, x):
        if x < self.A[0]:
            return 0
        return self.B.query(bisect.bisect_right(self.A,x) - 1)

    # find the k-th min_val (k:0-indexed)
    def __getitem__(self, k):
        if self.num <= k:
            ##### MINIMUM VAL #######
            return -10**9
        return self.A[self.B.lower_left(k+1)]

class UnionFind:
    def __init__(self, n:int):
        self.nodes = [i for i in range(n+1)]
        self.is_root = [True for i in range(n+1)]
        self.parent = [i for i in range(n+1)]

    def root(self, x:int) -> int:
        if self.is_root[x]:
            return x
        else:
            r = self.root(self.parent[x])
            self.parent[x] = r
            return r
    
    def unite(self, x:int, y:int) -> None:
        if self.same(x, y):
            return
        self.parent[y] = x
        self.is_root[y] = False
    
    def same(self, x:int, y:int) -> bool:
        if self.root(x) == self.root(y):
            return True
        return False

# =======================================================
#                        End
# =======================================================
if __name__=='__main__':
    main()