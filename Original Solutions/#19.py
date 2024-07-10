thirty_days = [3, 5, 8, 10]
thirty_one_days = [0, 2, 4, 6, 7, 9, 11]
start = 1
count = 0
for i in range(100):
    for k in range(12):
        if start % 7 == 6:
            count += 1
        if k in thirty_one_days:
            start += 3
        elif k in thirty_days:
            start += 2
        else:
            if i % 4 == 3:
                start += 1
print(count)
