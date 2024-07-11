spiral = [1]
for i in range(1, 501):
    for k in range(4):
        spiral.append((spiral[-1 - k] + 2 * i) + (k * 2 * i))
print(sum(spiral))