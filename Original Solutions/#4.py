max = 0
for i in range(100, 1000):
    for k in range(100, 1000):
        product = i * k
        if str(product)[0] == str(product)[-1]:
            if str(product)[1] == str(product)[-2]:
                if len(str(product)) == 5:
                    if product > max:
                        max = product
                else:
                    if str(product)[2] == str(product)[-3]:
                        if product > max:
                            max = product

print(max)