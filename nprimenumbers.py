def print_n_primes(n):
    primes = []
    sieve = [True] * (n * 10)  # Using a larger sieve to ensure we have enough primes

    # Mark 0 and 1 as non-prime
    sieve[0] = sieve[1] = False

    for i in range(2, int(n * 10 ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n * 10, i):
                sieve[j] = False

    # Collect the prime numbers
    for i, is_prime in enumerate(sieve):
        if is_prime:
            primes.append(i)
            if len(primes) == n:
                break

    # Print the prime numbers
    for prime in primes:
        print(prime)
print_n_primes(20)