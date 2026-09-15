"""
Problem: Koko Eating Bananas
Difficulty: Medium | Pattern: Binary search on the answer
Source: LeetCode 875

Koko has piles of bananas, piles[i] in the i-th pile. The guards return in h hours. Each
hour Koko picks a pile and eats k bananas from it; if the pile has fewer than k, she eats
the whole pile and waits until the next hour. Return the minimum integer speed k such that
she can eat all bananas within h hours.

Example 1:
  Input: piles = [3,6,7,11], h = 8
  Output: 4

Example 2:
  Input: piles = [30,11,23,4,20], h = 5
  Output: 30

Example 3:
  Input: piles = [30,11,23,4,20], h = 6
  Output: 23

Constraints:
  1 <= len(piles) <= 10^4
  len(piles) <= h <= 10^9
  1 <= piles[i] <= 10^9

Hints:
1. For a given speed k, hours needed = sum(ceil(p / k)) = sum((p + k - 1) // k). O(n) to check.
2. If speed k works, every larger speed works too: the predicate is monotonic.
3. Binary search k in [1, max(piles)] for the smallest k where hours <= h.

Expected: O(n log(max(piles))) time, O(1) space.
"""


def min_eating_speed(piles: list[int], h: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    assert min_eating_speed([1], 1) == 1
    assert min_eating_speed([1000000000], 2) == 500000000
    assert min_eating_speed([5, 5, 5], 3) == 5
    assert min_eating_speed([5, 5, 5], 100) == 1
    assert min_eating_speed([312884470], 968709470) == 1
    print("ok")
