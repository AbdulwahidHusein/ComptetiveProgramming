def sieve(n):
    siev = [True] * (n+1)
    sieve[0] = sieve[1] = False

    while p**2 <= n:
        if sieve[p]:
            for i in range(p**2, n+1, p):
                sieve[i] = False
        p += 1
    return siev

arr = sieve(20000000)

n = int(input())
nth = 2
