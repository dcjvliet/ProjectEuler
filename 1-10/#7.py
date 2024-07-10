import math


def find_primes(num):
    primes = [2]
    i = 3
    while i <= 2 ** num:
        lim = math.ceil(math.sqrt(i))
        prime = True
        for prime in primes:
            if prime <= lim:
                if i % prime == 0:
                    prime = False
                    break
        if prime:
            primes.append(i)
        if len(primes) == num:
            break
        i += 1
    return primes


print(find_primes(10001)[-1])