# Define a faster fibonacci procedure that will enable us to computer
# fibonacci(36).


def faster_fibonacci(n):
    result = 0
    x = 0
    y = 1
    while n > 1:
        result = x + y
        x, y = y, result
        n -= 1
    return result


def faster_fibonacci_2(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = faster_fibonacci_2(n - 1) + faster_fibonacci_2(n - 2)
    return cache[n]


print faster_fibonacci(36)
# >>> 14930352

print faster_fibonacci_2(36)
