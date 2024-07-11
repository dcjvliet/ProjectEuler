f=(lambda n,l=[1]:l if len(l)==n else (f(n,l+[l[-1]+(2*((len(l)-1)//4+1))])))
print(sum([n for n in f(2001,f(1400,[n for n in f(700)]))]))
