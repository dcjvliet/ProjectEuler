def fibonacci(digit_count):
    start = [1, 2]
    last_last = 1
    last = 2
    while len(str(start[-1])) != digit_count:
        start.append(last_last + last)
        last = start[-1]
        last_last = start[-2]
    return len(start)


print(fibonacci(1000))
