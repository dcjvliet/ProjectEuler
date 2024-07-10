fibonacci = [1, 2]
while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
print(sum([fibonacci[i] for i in range(len(fibonacci)) if fibonacci[i] % 2 == 0]))

# This is still a work in progress I know it can be shortened
