"""
Problem: Bit tricks
Difficulty: Easy | Topic: &, |, ^, <<, >>, x & (x-1), x & -x
Source: LeetCode 191, 231, 136, 338, 268

Do not use bin(), str formatting, or int.bit_count() for 1-2; use the bit operators.

1. count_bits(x) -> number of 1 bits in a non-negative int. Use Kernighan: x &= x - 1 clears the
   lowest set bit; count how many times until 0.
2. is_power_of_two(x) -> True iff x > 0 and x has exactly one set bit. O(1), no loop.
3. lowest_set_bit(x) -> the value of the lowest set bit (8 for 0b11000). 0 for x == 0.
4. single_number(nums) -> the one value that appears exactly once when every other appears twice. Use XOR, O(1) space.
5. missing_number(nums) -> nums contains n distinct numbers from 0..n; return the missing one. Use XOR, no sum().
6. get_bit(x, k), set_bit(x, k), clear_bit(x, k), toggle_bit(x, k) -> bit k (0 = least significant).
7. count_bits_upto(n) -> list where item i is count_bits(i), for i in 0..n, in O(n) using
   bits[i] = bits[i >> 1] + (i & 1).
8. subsets_by_mask(items) -> all subsets as lists, ordered by mask 0..2^n - 1, item i included
   iff bit i of the mask is set. subsets_by_mask(["a","b"]) -> [[], ["a"], ["b"], ["a","b"]].

Hints:
2. x > 0 and x & (x - 1) == 0
3. x & -x
5. XOR all indexes 0..n and all values; pairs cancel, the missing one remains.
"""


def count_bits(x: int) -> int:
    raise NotImplementedError


def is_power_of_two(x: int) -> bool:
    raise NotImplementedError


def lowest_set_bit(x: int) -> int:
    raise NotImplementedError


def single_number(nums: list[int]) -> int:
    raise NotImplementedError


def missing_number(nums: list[int]) -> int:
    raise NotImplementedError


def get_bit(x: int, k: int) -> int:
    raise NotImplementedError


def set_bit(x: int, k: int) -> int:
    raise NotImplementedError


def clear_bit(x: int, k: int) -> int:
    raise NotImplementedError


def toggle_bit(x: int, k: int) -> int:
    raise NotImplementedError


def count_bits_upto(n: int) -> list[int]:
    raise NotImplementedError


def subsets_by_mask(items: list) -> list[list]:
    raise NotImplementedError


if __name__ == "__main__":
    assert count_bits(0) == 0 and count_bits(1) == 1 and count_bits(0b1011) == 3 and count_bits(2**64 - 1) == 64, 'Check: count_bits(0) == 0 and count_bits(1) == 1 and count_bits(0b1011) == 3 and count_bits(2**64 - 1) == 64'
    assert all(count_bits(x) == bin(x).count("1") for x in range(1000)), 'Check: all(count_bits(x) == bin(x).count("1") for x in range(1000))'
    assert [x for x in range(-2, 70) if is_power_of_two(x)] == [1, 2, 4, 8, 16, 32, 64], 'Check: [x for x in range(-2, 70) if is_power_of_two(x)] == [1, 2, 4, 8, 16, 32, 64]'
    assert is_power_of_two(2**100) and not is_power_of_two(0), 'Check: is_power_of_two(2**100) and not is_power_of_two(0)'
    assert lowest_set_bit(0b11000) == 8 and lowest_set_bit(7) == 1 and lowest_set_bit(0) == 0 and lowest_set_bit(2**40) == 2**40, 'Check: lowest_set_bit(0b11000) == 8 and lowest_set_bit(7) == 1 and lowest_set_bit(0) == 0 and lowest_set_bit(2**40) == 2**40'
    assert single_number([4, 1, 2, 1, 2]) == 4 and single_number([7]) == 7 and single_number([-3, 5, 5]) == -3, 'Check: single_number([4, 1, 2, 1, 2]) == 4 and single_number([7]) == 7 and single_number([-3, 5, 5]) == -3'
    assert missing_number([3, 0, 1]) == 2 and missing_number([0]) == 1 and missing_number([1]) == 0, 'Check: missing_number([3, 0, 1]) == 2 and missing_number([0]) == 1 and missing_number([1]) == 0'
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8, 'Check: missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8'
    x = 0b1010
    assert get_bit(x, 1) == 1 and get_bit(x, 0) == 0, 'Check: get_bit(x, 1) == 1 and get_bit(x, 0) == 0'
    assert set_bit(x, 0) == 0b1011 and set_bit(x, 1) == x, 'Check: set_bit(x, 0) == 0b1011 and set_bit(x, 1) == x'
    assert clear_bit(x, 1) == 0b1000 and clear_bit(x, 0) == x, 'Check: clear_bit(x, 1) == 0b1000 and clear_bit(x, 0) == x'
    assert toggle_bit(x, 0) == 0b1011 and toggle_bit(x, 3) == 0b0010, 'Check: toggle_bit(x, 0) == 0b1011 and toggle_bit(x, 3) == 0b0010'
    assert count_bits_upto(5) == [0, 1, 1, 2, 1, 2] and count_bits_upto(0) == [0], 'Check: count_bits_upto(5) == [0, 1, 1, 2, 1, 2] and count_bits_upto(0) == [0]'
    assert count_bits_upto(1000) == [bin(i).count("1") for i in range(1001)], 'Check: count_bits_upto(1000) == [bin(i).count("1") for i in range(1001)]'
    assert subsets_by_mask(["a", "b"]) == [[], ["a"], ["b"], ["a", "b"]], 'Check: subsets_by_mask(["a", "b"]) == [[], ["a"], ["b"], ["a", "b"]]'
    assert subsets_by_mask([]) == [[]] and len(subsets_by_mask(list(range(10)))) == 1024, 'Check: subsets_by_mask([]) == [[]] and len(subsets_by_mask(list(range(10)))) == 1024'
    assert subsets_by_mask([1, 2, 3])[5] == [1, 3], 'Check: subsets_by_mask([1, 2, 3])[5] == [1, 3]'
    print("ok")
