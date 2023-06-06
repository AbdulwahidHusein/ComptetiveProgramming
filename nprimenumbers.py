def isPrime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
def countPrimes(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False

    p = 2
    while p**2 <= n:
        if sieve[p]:
            for i in range(p**2, n+1, p):
                sieve[i] = False
        p += 1

    count = sum(sieve)
    return count

n, m  = (int(j) for j in input().split())
count = countPrimes(n)
print(count)
for i in range(m):
    aa = int(input())
    if isPrime(aa):
        print(1)
    else:
        print(0)
