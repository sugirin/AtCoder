"""
https://atcoder.jp/contests/abc217/tasks/abc217_e
"""

import math
import heapq
from collections import deque
from typing import List, Tuple

def main():
    Q = int(input())
    # N, M = map(int, input().split())
    # S = input()
    # T = list(map(int, input().split()))
    l = []
    heapq.heapify(l)
    r = deque([])
    for _ in range(Q):
        q = input()
        if q[0] == '1':
            x = int(q.split()[1])
            r.append(x)
        elif q[0] == '2':
            if l:
                x = heapq.heappop(l)
            else:
                x = r.popleft()
            print(x)
        else:
            for x in r:
                heapq.heappush(l, x)
            r = deque([])

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
        List[Tuple[int, int]]: x = p1^q1 + p2^q2 + ... の時、 [(p1, q1), (p2, q2), ...] のlist
    
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

# =======================================================
#                        End
# =======================================================
if __name__=='__main__':
    main()