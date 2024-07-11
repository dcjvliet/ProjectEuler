total = 0
for i in range(2, 1000000): # this range was a random guess
    sum = 0
    for char in str(i):
        sum += int(char) ** 5
    if sum == i:
        total += i
print(total)
