import math


def triangle_num(num):
    return num * (num + 1) / 2


def factors(num):
    factors = [1, num]
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            # double count so you get the larger factor as well.
            factors.append(i)
            factors.append(i)
    return len(factors)


found = False
i = 500
while not found:
    numero = factors(triangle_num(i))
    if numero > 500:
        found = True
        print(triangle_num(i))
    i += 1