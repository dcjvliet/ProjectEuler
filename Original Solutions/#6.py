def square_sum(n):
    return n * (n + 1) * (2 * n + 1) / 6


def sum_squared(n):
    return (n * (n + 1) / 2) ** 2


print(abs(sum_squared(100) - square_sum(100)))