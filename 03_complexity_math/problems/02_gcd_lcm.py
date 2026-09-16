"""
Problem: gcd and lcm
Difficulty: Warm-up | Topic: Euclid's algorithm, number theory
Source: LeetCode 1979, 2413 (variants)

Do NOT use math.gcd or math.lcm here; write Euclid yourself.

1. gcd(a, b) for non-negative ints. gcd(0, 0) == 0, gcd(a, 0) == a.
2. lcm(a, b). lcm(0, x) == 0.
3. gcd_list(nums) -> gcd of all items (nums non-empty).
4. lcm_list(nums) -> lcm of all items.
5. are_coprime(a, b) -> gcd == 1.
6. reduce_fraction(num, den) -> (num, den) in lowest terms with den > 0. den != 0.
   reduce_fraction(6, -4) -> (-3, 2); reduce_fraction(0, 5) -> (0, 1).

Hints:
1. while b: a, b = b, a % b
2. a // gcd(a, b) * b avoids the large intermediate product.
3. functools.reduce(gcd, nums) or a plain loop.
6. Divide by gcd(abs(num), abs(den)), then flip both signs if den < 0.
"""
from functools import reduce


def gcd(a: int, b: int) -> int:
    raise NotImplementedError


def lcm(a: int, b: int) -> int:
    raise NotImplementedError


def gcd_list(nums: list[int]) -> int:
    raise NotImplementedError


def lcm_list(nums: list[int]) -> int:
    raise NotImplementedError


def are_coprime(a: int, b: int) -> bool:
    raise NotImplementedError


def reduce_fraction(num: int, den: int) -> tuple[int, int]:
    raise NotImplementedError


if __name__ == "__main__":
    import math
    assert gcd(12, 18) == 6 and gcd(18, 12) == 6 and gcd(7, 13) == 1, 'Check: gcd(12, 18) == 6 and gcd(18, 12) == 6 and gcd(7, 13) == 1'
    assert gcd(0, 5) == 5 and gcd(5, 0) == 5 and gcd(0, 0) == 0, 'Check: gcd(0, 5) == 5 and gcd(5, 0) == 5 and gcd(0, 0) == 0'
    assert gcd(2**60, 2**40 * 3) == 2**40, 'Check: gcd(2**60, 2**40 * 3) == 2**40'
    for a in range(0, 30):
        for b in range(0, 30):
            assert gcd(a, b) == math.gcd(a, b), (a, b)
    assert lcm(4, 6) == 12 and lcm(0, 9) == 0 and lcm(7, 1) == 7, 'Check: lcm(4, 6) == 12 and lcm(0, 9) == 0 and lcm(7, 1) == 7'
    assert gcd_list([12, 18, 24]) == 6 and gcd_list([5]) == 5 and gcd_list([0, 0, 7]) == 7, 'Check: gcd_list([12, 18, 24]) == 6 and gcd_list([5]) == 5 and gcd_list([0, 0, 7]) == 7'
    assert lcm_list([2, 3, 4]) == 12 and lcm_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2520, 'Check: lcm_list([2, 3, 4]) == 12 and lcm_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2520'
    assert are_coprime(8, 9) and not are_coprime(8, 12) and are_coprime(1, 1), 'Check: are_coprime(8, 9) and not are_coprime(8, 12) and are_coprime(1, 1)'
    assert reduce_fraction(6, 4) == (3, 2) and reduce_fraction(6, -4) == (-3, 2), 'Check: reduce_fraction(6, 4) == (3, 2) and reduce_fraction(6, -4) == (-3, 2)'
    assert reduce_fraction(0, 5) == (0, 1) and reduce_fraction(-3, -9) == (1, 3) and reduce_fraction(5, 5) == (1, 1), 'Check: reduce_fraction(0, 5) == (0, 1) and reduce_fraction(-3, -9) == (1, 3) and reduce_fraction(5, 5) == (1, 1)'
    print("ok")
