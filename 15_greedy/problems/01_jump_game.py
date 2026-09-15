"""
Problem: Jump Game
Difficulty: Medium | Pattern: Greedy (track farthest reach)
Source: LeetCode 55

You are given an integer array nums. You start at index 0 and nums[i] is the maximum
jump length from index i. Return True if you can reach the last index.

Example 1: nums = [2, 3, 1, 1, 4] -> True   (0 -> 1 -> 4)
Example 2: nums = [3, 2, 1, 0, 4] -> False  (you always land on index 3, which has 0)
Example 3: nums = [0] -> True (already at the last index)

Hints:
1. Keep `farthest`, the largest index reachable so far.
2. Scanning i from left to right: if i > farthest you are stuck; otherwise farthest = max(farthest, i + nums[i]).
3. Exchange argument: being able to reach farther never hurts, so tracking the max is safe.

Expected: O(n) time, O(1) space
"""


def can_jump(nums: list[int]) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False
    assert can_jump([0]) is True
    assert can_jump([1, 0]) is True
    assert can_jump([0, 1]) is False
    assert can_jump([2, 0, 0]) is True
    assert can_jump([1, 1, 1, 0]) is True
    assert can_jump([5, 0, 0, 0, 0, 0]) is True
    print("ok")
