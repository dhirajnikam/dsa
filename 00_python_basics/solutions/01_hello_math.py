def average(a, b):
    return (a + b) / 2


def digits_sum(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total


def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def celsius_to_f(c):
    return round(c * 9 / 5 + 32, 1)
