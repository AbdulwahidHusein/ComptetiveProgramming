#prime seive
def primeFactors(n):
    def isPrime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    if isPrime(n):
        return [n]

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    while n % 3 == 0:
        factors.append(3)
        n //= 3

    while n % 5 == 0:
        factors.append(5)
        n //= 5

    i = 7
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 2

    if n > 1:
        factors.append(n)

    return factors

    
'''def prime_factors(n):
    sieve = [0] * (n + 1)
    prime_factors = []

    for i in range(2, n + 1):
        if sieve[i] == 0:  # i is a prime number
            for j in range(i, n + 1, i):
                if sieve[j] == 0:  # j has not been marked yet
                    sieve[j] = i  # mark j with i as its smallest prime factor

    while n > 1:
        prime_factor = sieve[n]
        prime_factors.append(prime_factor)
        n //= prime_factor

    return prime_factors'''

n = int(input())
while n!=-1:
    s = ''
    pf = primeFactors(n)
    l = ' '.join([str(p) for p in pf])
    print(l.strip())
    n = int(input())

    



