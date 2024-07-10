def num_to_words(num):
    words = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen',14 : 'fourteen', 
             15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety', 100 : 'hundred'}
    if 0 < num < 21:
        return words[num]
    elif 20 < num < 100:
        tens = words[(num // 10) * 10]
        ones = ''
        if num % 10 != 0:
            ones = words[num % 10]
        return tens + ones
    elif 99 < num < 1000:
        hundreds = words[num // 100] + words[100]
        additive = ''
        if num % 100 != 0:
            additive = 'and'
        tens = ''
        ones = ''
        if int(str(num)[1]) > 1:
            tens = words[int(str(num)[1]) * 10]
            if int(str(num)[2]) != 0:
                ones = words[int(str(num)[2])]
        elif int(str(num)[1]) == 1:
            tens = words[int(str(num)[1:3])]
        elif int(str(num)[1]) == 0 and int(str(num)[2]) != 0:
            ones = words[int(str(num)[2])]
        return hundreds + additive + tens + ones
    elif num == 1000:
        return 'onethousand'
    elif num == 0:
        print('Number too small')
    else:
        print('Number too large')
    

sum = 0
for i in range(1, 1001):
    sum += len(num_to_words(i))
print(sum)
