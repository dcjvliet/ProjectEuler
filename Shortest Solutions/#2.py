l = (lambda n,f=[1,1]:f if len(f)==n else (l(n,f+[f[-1]+f[-2]])))
print(sum([n for n in l(200) if n%2==0 and n<4000000]))
