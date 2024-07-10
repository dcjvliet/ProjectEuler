f=[1,2]
while f[-1]<4000000:
    f.append(f[-2]+f[-1])
print(sum([f[i] for i in range(len(f)) if f[i]%2==0]))

# This is still a work in progress I know it can be shortened
