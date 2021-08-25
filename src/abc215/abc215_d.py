"""
https://atcoder.jp/contests/abc215/tasks/abc215_d
"""
def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))

    M_list = [True for _ in range(M+1)]
    M_list[0] = False

    factor_set = set()
    for a in A:
        a_factor = factorization(a)
        for af, cnt in a_factor:
            factor_set.add(af)

    factor_list = sorted(list(factor_set))
    for p in factor_list:
        for i in range((M//p)+1):
            M_list[p*i] = False

    print(sum(M_list))
    for i, m in enumerate(M_list):
        if m:
            print(i)

import math

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    prime_list = []
    for i, p in enumerate(prime):
        if p:
            prime_list.append(i)
    return prime_list

def factorization(n):
    factor = []
    for i in range(2, n):
        if i*i > n:
            break
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            factor.append([i, cnt])
    
    if n != 1:
        factor.append([n, 1])

    return factor

if __name__=='__main__':
    main()