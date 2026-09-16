"""
Problem: Jump Game II
Difficulty: Medium | Pattern: Greedy (BFS levels over indices)
Source: LeetCode 45

Given nums where nums[i] is the maximum jump length from index i, return the minimum
number of jumps to reach the last index. You can assume the last index is reachable.

Example 1: nums = [2, 3, 1, 1, 4] -> 2   (0 -> 1 -> 4)
Example 2: nums = [2, 3, 0, 1, 4] -> 2
Example 3: nums = [0] -> 0

Hints:
1. Think BFS: all indices reachable with j jumps form a contiguous range [start, end].
2. Walk i through the current range and compute farthest = max(i + nums[i]).
3. When i == end, one more jump is needed and the new end is farthest. Loop i to n-2 only.

Expected: O(n) time, O(1) space
"""


def jump(nums: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert jump([2, 3, 1, 1, 4]) == 2, 'Check: jump([2, 3, 1, 1, 4]) == 2'
    assert jump([2, 3, 0, 1, 4]) == 2, 'Check: jump([2, 3, 0, 1, 4]) == 2'
    assert jump([0]) == 0, 'Check: jump([0]) == 0'
    assert jump([1, 2]) == 1, 'Check: jump([1, 2]) == 1'
    assert jump([1, 1, 1, 1]) == 3, 'Check: jump([1, 1, 1, 1]) == 3'
    assert jump([5, 1, 1, 1, 1, 1]) == 1, 'Check: jump([5, 1, 1, 1, 1, 1]) == 1'
    assert jump([1, 2, 1, 1, 1]) == 3, 'Check: jump([1, 2, 1, 1, 1]) == 3'
    assert jump([4, 1, 1, 3, 1, 1, 1]) == 2, 'Check: jump([4, 1, 1, 3, 1, 1, 1]) == 2'
    print("ok")
