"""
Problem: Candy
Difficulty: Hard | Pattern: Greedy (two passes)
Source: LeetCode 135

There are n children in a line with ratings[i]. Each child gets at least one candy, and a
child with a higher rating than an adjacent child must get more candies than that
neighbour. Return the minimum total number of candies.

Example 1: ratings = [1, 0, 2] -> 5   (candies [2, 1, 2])
Example 2: ratings = [1, 2, 2] -> 4   (candies [1, 2, 1]; equal ratings have no constraint)

Hints:
1. Start everyone at 1.
2. Left-to-right pass: if ratings[i] > ratings[i-1], candy[i] = candy[i-1] + 1.
3. Right-to-left pass: if ratings[i] > ratings[i+1], candy[i] = max(candy[i], candy[i+1] + 1).
   The max keeps the left constraint intact while fixing the right one.
4. Follow-up if asked: an O(1) space solution exists by counting up/down slope lengths.

Expected: O(n) time, O(n) space
"""


def candy(ratings: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert candy([1, 0, 2]) == 5
    assert candy([1, 2, 2]) == 4
    assert candy([1]) == 1
    assert candy([2, 2, 2, 2]) == 4
    assert candy([1, 2, 3, 4]) == 10
    assert candy([4, 3, 2, 1]) == 10
    assert candy([1, 3, 2, 2, 1]) == 7
    assert candy([1, 2, 87, 87, 87, 2, 1]) == 13
    print("ok")
