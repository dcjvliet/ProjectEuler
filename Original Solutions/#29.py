powers = []
for a in range(2, 101):
    for b in range(2, 101):
        power = a ** b
        if power not in powers:
            powers.append(power)
print(len(powers))