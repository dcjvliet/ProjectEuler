sum = 0
for i in range(1, 1001):
    sum += i ** i
print(str(sum)[len(str(sum)) - 10:])