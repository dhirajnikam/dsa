"""
Problem: Counting Bits
Difficulty: Easy | Pattern: Bit manipulation DP
Source: LeetCode 338

Given n, return an array ans of length n + 1 where ans[i] is the number of 1 bits in the
binary representation of i.

Example 1: n = 2 -> [0, 1, 1]
Example 2: n = 5 -> [0, 1, 1, 2, 1, 2]

Hints:
1. bits[i] = bits[i >> 1] + (i & 1): dropping the last bit gives a smaller, already-solved i.
2. Or bits[i] = bits[i & (i - 1)] + 1: clearing the lowest set bit (Brian Kernighan).
3. bin(i).count("1") per element is O(n log n) and fine as a first answer; the DP is the
   follow-up the interviewer wants.

Expected: O(n) time, O(n) space for the output
"""


def count_bits(n: int) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert count_bits(0) == [0], 'Check: count_bits(0) == [0]'
    assert count_bits(1) == [0, 1], 'Check: count_bits(1) == [0, 1]'
    assert count_bits(2) == [0, 1, 1], 'Check: count_bits(2) == [0, 1, 1]'
    assert count_bits(5) == [0, 1, 1, 2, 1, 2], 'Check: count_bits(5) == [0, 1, 1, 2, 1, 2]'
    assert count_bits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1], 'Check: count_bits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]'
    assert count_bits(15)[15] == 4, 'Check: count_bits(15)[15] == 4'
    assert count_bits(1000) == [bin(i).count("1") for i in range(1001)], 'Check: count_bits(1000) == [bin(i).count("1") for i in range(1001)]'
    print("ok")
