sums = []
for i in range(10000):
    for k in range(10000):
        if i * k < 100000:
            chars = []
            for char in str(i):
                chars.append(int(char))
            for char in str(k):
                chars.append(int(char))
            for char in str(i * k):
                chars.append(int(char))
            chars.sort()
            if chars == [1, 2, 3, 4, 5, 6, 7, 8, 9] and i * k not in sums:
                sums.append(i * k)
print(sum(sums))
