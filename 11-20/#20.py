from math import factorial


sum = 0
for char in str(factorial(100)):
    sum += int(char)
print(sum)