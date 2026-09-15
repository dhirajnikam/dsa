"""
Problem: Product of Array Except Self
Difficulty: Medium | Pattern: prefix and suffix products
Source: LeetCode 238

Given an integer array nums, return an array answer such that answer[i] is the product
of all elements of nums except nums[i]. Do NOT use division. Must run in O(n).

Example 1:
  nums = [1, 2, 3, 4] -> [24, 12, 8, 6]
Example 2:
  nums = [-1, 1, 0, -3, 3] -> [0, 0, 9, 0, 0]

Constraints:
  2 <= len(nums) <= 10^5
  -30 <= nums[i] <= 30
  The product of any prefix or suffix fits in a 32-bit integer.

Hints:
1. answer[i] = (product of everything left of i) * (product of everything right of i).
2. Fill answer with left products in one forward pass.
3. Walk backwards with a running right product and multiply it in. O(1) extra space.

Expected: O(n) time, O(1) extra space (output array not counted)
"""


def product_except_self(nums: list[int]) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([2, 3]) == [3, 2]
    assert product_except_self([0, 0]) == [0, 0]
    assert product_except_self([5, 0]) == [0, 5]
    assert product_except_self([1, 1, 1]) == [1, 1, 1]
    assert product_except_self([-2, -3, 4]) == [-12, -8, 6]
    print("ok")
