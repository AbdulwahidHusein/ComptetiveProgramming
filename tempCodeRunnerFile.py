#prime seive

def isp(n):
    for i in range(2, int(n**0.5)+1):
        if n%i ==0:
            return False
    return True
def prmf(n):
    if isp(n):
        return [n]
    prmfs = []
    while n%2==0:
        prmfs.append(2)
        n//=2
    while n%3==0:
        prmfs.append(3)
        n//=3
    while n%5==0:
        prmfs.append(5)
        n//=5
    for i in range(5, int(n/2)+1, 2):
        if n%i!=3 and n%i!=2:
            while n%i==0:
                prmfs.append(i)
                n//=i
    return prmfs
    
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
    pf = prmf(n)
    print(' '.join([str(p) for p in pf]))
    n = int(input())

    



