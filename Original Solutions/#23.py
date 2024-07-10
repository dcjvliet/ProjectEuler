import math


def factors(num):
    factors = [1, num]
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            # double count so you get the larger factor as well.
            factors.append(i)
            factors.append(int(num / i))
    return list(set(factors))


def find_abundants(lim):
    abundants = []
    for i in range(12, lim):
        sum = 0
        for factor in factors(i):
            sum += factor
        if sum - i > i:
            abundants.append(i)
    return abundants


abundants = find_abundants(28124)
sums = []
for num1 in abundants:
    for num2 in abundants:
        sum = num1 + num2
        if sum < 28124:
            sums.append(sum)
sum = 0
sums = list(set(sums))
for i in range(28124):
    if i not in sums:
        sum += i
print(sum)
