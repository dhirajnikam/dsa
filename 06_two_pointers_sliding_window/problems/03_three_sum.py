"""
Problem: 3Sum
Difficulty: Medium | Pattern: sort + fix one + two pointers, skip duplicates
Source: LeetCode 15

Given an integer array nums, return all unique triplets [a, b, c] with a + b + c == 0.
Triplets may be returned in any order and any internal order, but the SET of triplets must
contain no duplicates.

Example 1:
  nums = [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]]
Example 2:
  nums = [0, 1, 1] -> []
Example 3:
  nums = [0, 0, 0] -> [[0, 0, 0]]

Constraints:
  3 <= len(nums) <= 3000
  -10^5 <= nums[i] <= 10^5

Hints:
1. Sort first. Fix index i, then solve Two Sum (sorted) on the range i+1..n-1 with target -nums[i].
2. Skip duplicate values for i (if nums[i] == nums[i-1]: continue) to avoid duplicate triplets.
3. After finding a triplet, advance l past equal values and r past equal values.
   Stop early when nums[i] > 0 (everything after is positive).

Expected: O(n^2) time, O(1) extra space (ignoring sort and output)
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    raise NotImplementedError


if __name__ == "__main__":
    def norm(triplets):
        return sorted(sorted(t) for t in triplets)

    assert norm(three_sum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert norm(three_sum([0, 1, 1])) == []
    assert norm(three_sum([0, 0, 0])) == [[0, 0, 0]]
    assert norm(three_sum([0, 0, 0, 0])) == [[0, 0, 0]]
    assert norm(three_sum([1, 2, 3])) == []
    assert norm(three_sum([-2, 0, 1, 1, 2])) == [[-2, 0, 2], [-2, 1, 1]]
    assert norm(three_sum([-1, -1, -1, 2, 2])) == [[-1, -1, 2]]
    assert norm(three_sum([3, -2, 1, 0])) == []
    assert norm(three_sum([-4, -2, -2, 0, 0, 2, 2, 4])) == [[-4, 0, 4], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
    print("ok")
