"""
https://atcoder.jp/contests/abc216/tasks/abc216_a
"""

import math
from typing import List, Tuple

def main():
    X, Y = map(int, input().split('.'))
    if Y <= 2:
        print(f'{X}-')
    elif Y >= 7:
        print(f'{X}+')
    else:
        print(X)



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