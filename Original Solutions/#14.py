def collatz(num):
    i = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        i += 1
    return i


max = 0
index = 0
for i in range(2, 1000000):
    temp = collatz(i)
    if temp > max:
        max = temp
        index = i

print(index)