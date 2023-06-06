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


n = int(input())
while n!=-1:
    s = ''
    pf = primeFactors(n)
    l = ' '.join([str(p) for p in pf])
    print(l+' ')
    n = int(input())

    



