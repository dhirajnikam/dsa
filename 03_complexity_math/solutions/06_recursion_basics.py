import sys

sys.setrecursionlimit(20000)


def factorial(n):  # O(n) time, O(n) stack
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_digits(n):  # O(number of digits)
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


def reverse_string(s):  # O(n^2) because of slicing; fine for learning
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])


def power_set_size(n):  # O(n): each element doubles the count
    if n == 0:
        return 1
    return 2 * power_set_size(n - 1)


def sum_list(nums):  # O(n) time, O(n) stack; index recursion avoids O(n^2) slicing
    def go(i):
        if i == len(nums):
            return 0
        return nums[i] + go(i + 1)
    return go(0)


def count_down(n):
    if n == 0:
        return []
    return [n] + count_down(n - 1)


def depth_of_nested(lst):
    if not isinstance(lst, list):
        return 0
    return 1 + max((depth_of_nested(x) for x in lst), default=0)
