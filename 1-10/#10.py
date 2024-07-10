import math


def find_primes(num):
    primes = [2]
    i = 3
    lim = 30
    while i <= num:
        if i % 900 == 0:
            lim = math.ceil(math.sqrt(i + 900))
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


primes = find_primes(2000000)
sum = 0
for prime in primes:
    sum += prime
print(sum)