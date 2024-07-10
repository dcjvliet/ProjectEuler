import math


def factors(num):
    factors = [1, num]
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            # double count so you get the larger factor as well.
            factors.append(i)
            factors.append(int(num / i))
    return factors


total_sum = 0
for i in range(2, 10001):
    sum = 0
    alt_sum = 0
    for factor in factors(i):
        sum += factor
    sum -= i
    for factor in factors(sum):
        alt_sum += factor
    alt_sum -= sum
    if alt_sum == i and sum != i:
        total_sum += i
print(total_sum)