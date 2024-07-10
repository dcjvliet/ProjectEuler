def fibonacci(end):
    start = [1, 2]
    last_last = 1
    last = 2
    while last_last + last < end:
        sum = last_last + last
        start.append(sum)
        last_last = last
        last = sum
    return start


nums = fibonacci(4000000)
sum = 0
for num in nums:
    if num % 2 == 0:
        sum += num

print(sum)
