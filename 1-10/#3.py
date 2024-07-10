import math


def find_primes(num):
    primes = [2]
    i = 3
    while i <= num:
        lim = math.ceil(math.sqrt(i))
        prime = True
        for prime in primes:
            if prime <= lim:
                if i % prime == 0:
                    prime = False
                    break
        if prime:
            primes.append(i)
        i += 1
    return primes


def max_prime_factor(num):
    lim = math.ceil(math.sqrt(num))
    primes = find_primes(lim)
    max = 1
    for prime in primes:
        if num % prime == 0:
            max = prime
    return max


print(max_prime_factor(600851475143))