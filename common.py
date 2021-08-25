
import math

def main():
    pass


# =======================================================
#                       Utilities
# =======================================================
def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    primes[0] = False
    primes[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = False
    return primes

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
    
    # sqrt(n)まで試し割りして割り切れなかった時
    if n != 1:
        factor.append([n, 1])

    return factor

# =======================================================
#                        End
# =======================================================
if __name__=='__main__':
    main()