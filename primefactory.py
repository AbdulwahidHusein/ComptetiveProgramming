def primeFactors(n):
    def isPrime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    if isPrime(n):
        return str(n) + ' '

    factors = ''
    while n % 2 == 0:
        factors += '2 '
        n //= 2

    while n % 3 == 0:
        factors += '3 '
        n //= 3

    while n % 5 == 0:
        factors += '5 '
        n //= 5

    i = 7
    while i * i <= n:
        if n % i == 0:
            factors += str(i) + ' '
            n //= i
        else:
            i += 2

    if n > 1:
        factors += str(n) + ' '

    return factors


inputs = []
while True:
    num = int(input())
    if num == -1:
        break
    inputs.append(num)
    
for num in inputs:
    factors = primeFactors(num)
    print(factors.strip())
