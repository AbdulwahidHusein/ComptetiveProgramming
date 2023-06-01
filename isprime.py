
def isp(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
def n_primes(n):
    pr = 0
    aa = []
    sieve = [True] * n
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False

    for i, is_prime in enumerate(sieve):
        if is_prime:
            pr+=1
            aa.append(i)
    return aa

n, r  = [int(i) for i in input().split()]
print(n_primes(n))
for i in range(r):
    nn = int(input())
    if isp(nn):
        print(1)
    else:
        print(0)