"""
Problem: Basic arithmetic
Difficulty: Warm-up | Topic: ints, floats, operators

Implement each function using only arithmetic operators.

1. average(a, b): return the mean of two numbers as a float.
2. digits_sum(n): return the sum of the decimal digits of a non-negative int
   (e.g. 1234 -> 10). Use % and // in a loop, no str().
3. is_leap(year): True if divisible by 4, except centuries unless divisible by 400.
4. celsius_to_f(c): (c * 9/5) + 32 rounded to 1 decimal.

Hints:
1. n % 10 is the last digit, n // 10 drops it.
2. Order the leap-year checks from most specific (400) to least (4).
"""


def average(a, b):
    return (a + b) / 2


def digits_sum(n):
    total = 0
    while n > 0:
        total += (n % 10)
        n = n // 10

    return total



def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

def celsius_to_f(c):
    total = (c * 9/5) + 32
    return  round(total, 1)



if __name__ == "__main__":
    assert average(2, 3) == 2.5, 'Check: average(2, 3) == 2.5'
    assert average(10, 10) == 10.0, 'Check: average(10, 10) == 10.0'
    assert digits_sum(1234) == 10, 'Check: digits_sum(1234) == 10'
    assert digits_sum(0) == 0, 'Check: digits_sum(0) == 0'
    assert digits_sum(9999) == 36, 'Check: digits_sum(9999) == 36'
    assert is_leap(2000) and is_leap(2024) and not is_leap(1900) and not is_leap(2023), 'Check: is_leap(2000) and is_leap(2024) and not is_leap(1900) and not is_leap(2023)'
    assert celsius_to_f(100) == 212.0, 'Check: celsius_to_f(100) == 212.0'
    assert celsius_to_f(37) == 98.6, 'Check: celsius_to_f(37) == 98.6'
    # Boundary and misconception checks: predict each result before running.
    assert average(-6, 2) == -2.0, 'Check: average(-6, 2) == -2.0'
    assert isinstance(average(2, 2), float), 'Check: isinstance(average(2, 2), float)'
    assert digits_sum(10020) == 3, 'Check: digits_sum(10020) == 3'
    assert not is_leap(2100) and is_leap(2400), 'Check: not is_leap(2100) and is_leap(2400)'
    assert celsius_to_f(-40) == -40.0, 'Check: celsius_to_f(-40) == -40.0'
    print("ok")
