with open('names.txt', 'r') as f:
    content = f.readlines()
names = content[0].split(',')
cleaned = []
for name in names:
    cleaned.append(name[1:].rstrip('"\''))
cleaned = sorted(cleaned)
score_conv = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15,
         'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}
sum = 0
for i in range(len(cleaned)):
    score = 0
    for char in cleaned[i]:
        score += score_conv[char.lower()]
    sum += int(score) * (i + 1)
print(sum)