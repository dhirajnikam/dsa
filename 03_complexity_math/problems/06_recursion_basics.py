"""
Problem: Recursion basics
Difficulty: Easy | Topic: base case, recursive case, call stack, recursion depth

Every function must be recursive (no loops, no slicing tricks that hide the loop like ''.join(reversed())).
The tests check that the functions call themselves by counting frames.

1. factorial(n) -> n! for n >= 0.
2. sum_digits(n) -> sum of decimal digits of n >= 0. sum_digits(0) == 0.
3. reverse_string(s) -> reversed s. Base case: len(s) <= 1.
4. is_palindrome(s) -> compare first and last, recurse on the middle.
5. power_set_size(n) -> number of subsets of an n-element set, computed as
   power_set_size(n-1) * 2 (each element is in or out). power_set_size(0) == 1.
6. sum_list(nums) -> sum via index recursion helper (do not slice: sum_list on 5000 items must work).
   Bump sys.setrecursionlimit if you need to.
7. count_down(n) -> list [n, n-1, ..., 1] built recursively. count_down(0) == [].
8. depth_of_nested(lst) -> nesting depth of a list: depth_of_nested([]) == 1,
   depth_of_nested([1, [2, [3]]]) == 3, depth_of_nested(5) == 0 (a non-list has depth 0).

Hints:
2. sum_digits(n) = n % 10 + sum_digits(n // 10), base n == 0.
3. reverse_string(s[1:]) + s[0]
6. def go(i): return 0 if i == len(nums) else nums[i] + go(i + 1)
8. 1 + max(depth of each child, default 0)
"""
import sys

sys.setrecursionlimit(20000)


def factorial(n: int) -> int:
    raise NotImplementedError


def sum_digits(n: int) -> int:
    raise NotImplementedError


def reverse_string(s: str) -> str:
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    raise NotImplementedError


def power_set_size(n: int) -> int:
    raise NotImplementedError


def sum_list(nums: list[int]) -> int:
    raise NotImplementedError


def count_down(n: int) -> list[int]:
    raise NotImplementedError


def depth_of_nested(lst) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    import math

    assert factorial(0) == 1 and factorial(1) == 1 and factorial(5) == 120 and factorial(20) == math.factorial(20)
    assert sum_digits(0) == 0 and sum_digits(1234) == 10 and sum_digits(10**18) == 1
    assert reverse_string("") == "" and reverse_string("a") == "a" and reverse_string("abc") == "cba"
    assert reverse_string("hello world") == "dlrow olleh"
    assert is_palindrome("") and is_palindrome("a") and is_palindrome("abba") and is_palindrome("racecar")
    assert not is_palindrome("ab") and not is_palindrome("abca")
    assert power_set_size(0) == 1 and power_set_size(3) == 8 and power_set_size(20) == 2**20
    assert sum_list([]) == 0 and sum_list([5]) == 5 and sum_list([1, 2, 3]) == 6
    assert sum_list(list(range(5000))) == sum(range(5000))
    assert count_down(0) == [] and count_down(1) == [1] and count_down(4) == [4, 3, 2, 1]
    assert depth_of_nested(5) == 0 and depth_of_nested([]) == 1 and depth_of_nested([1, 2]) == 1
    assert depth_of_nested([1, [2, [3]]]) == 3 and depth_of_nested([[[]], []]) == 3

    # recursion check: a recursive factorial(50) reaches at least 50 frames deep
    max_depth = [0]

    def tracer(frame, event, arg):
        if event == "call":
            d, f = 0, frame
            while f is not None:
                d += 1
                f = f.f_back
            max_depth[0] = max(max_depth[0], d)
        return tracer

    base = 0
    f = sys._getframe()
    while f is not None:
        base += 1
        f = f.f_back
    sys.settrace(tracer)
    factorial(50)
    sys.settrace(None)
    assert max_depth[0] - base >= 50, "factorial must be recursive"
    print("ok")
