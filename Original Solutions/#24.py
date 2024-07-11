import math


def get_millionth_permutation(string):
    permutation = []
    k = 999999
    available_chars = list(string)
    
    while available_chars:
        n = len(available_chars)
        fact = math.factorial(n - 1)
        index = k // fact
        permutation.append(available_chars.pop(index))
        k %= fact
        
    return ''.join(permutation)


data = '0123456789'
print(get_millionth_permutation(data))
