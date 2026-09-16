"""
Problem: Maximum XOR of Two Numbers in an Array
Difficulty: Medium | Pattern: Trie over bits
Source: LeetCode 421

Given an integer array nums (0 <= nums[i] < 2^31), return max(nums[i] XOR nums[j]) over
all pairs i <= j.

Example 1: nums = [3, 10, 5, 25, 2, 8] -> 28   (5 XOR 25)
Example 2: nums = [0] -> 0
Example 3: nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70] -> 127

Hints:
1. Build a binary trie: each number is a 31-bit path from the MSB (bit 30) down to bit 0.
2. For each number, walk the trie preferring the child with the opposite bit at every
   level; that greedily maximises the XOR from the high bit down.
3. Alternative O(31 n) without a trie: build the answer bit by bit using a set of prefixes
   and the identity a ^ b = c  <=>  a ^ c = b.

Expected: O(31 n) time, O(31 n) space
"""


def find_maximum_xor(nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert find_maximum_xor([3, 10, 5, 25, 2, 8]) == 28, 'Check: find_maximum_xor([3, 10, 5, 25, 2, 8]) == 28'
    assert find_maximum_xor([0]) == 0, 'Check: find_maximum_xor([0]) == 0'
    assert find_maximum_xor([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]) == 127, 'Check: find_maximum_xor([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]) == 127'
    assert find_maximum_xor([1, 1]) == 0, 'Check: find_maximum_xor([1, 1]) == 0'
    assert find_maximum_xor([1, 2]) == 3, 'Check: find_maximum_xor([1, 2]) == 3'
    assert find_maximum_xor([2 ** 31 - 1, 0]) == 2 ** 31 - 1, 'Check: find_maximum_xor([2 ** 31 - 1, 0]) == 2 ** 31 - 1'
    assert find_maximum_xor([8, 10, 2]) == 10, 'Check: find_maximum_xor([8, 10, 2]) == 10'
    assert find_maximum_xor([5, 5, 5]) == 0, 'Check: find_maximum_xor([5, 5, 5]) == 0'
    print("ok")
