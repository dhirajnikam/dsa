"""
Problem: Find Median from Data Stream
Difficulty: Hard | Pattern: two heaps
Source: LeetCode 295

Design a class that supports adding integers from a stream and returning the median of
all elements so far. The median of an even count is the mean of the two middle values.

  MedianFinder()          initializes the structure
  add_num(num)            adds num
  find_median() -> float  returns the current median

Example:
  mf = MedianFinder(); mf.add_num(1); mf.add_num(2)
  mf.find_median() -> 1.5
  mf.add_num(3); mf.find_median() -> 2.0

Constraints:
  -10^5 <= num <= 10^5
  find_median is only called after at least one add_num
  Up to 5 * 10^4 calls

Hints:
1. Keep the smaller half in a max-heap (negated) and the larger half in a min-heap.
2. Invariant: len(low) == len(high) or len(low) == len(high) + 1. Push to low, move
   low's max to high, then if high is bigger move high's min back to low.
3. Median: -low[0] if sizes differ, else the average of -low[0] and high[0].

Expected: O(log n) add, O(1) median, O(n) space
"""
import heapq


class MedianFinder:
    def __init__(self):
        raise NotImplementedError

    def add_num(self, num: int) -> None:
        raise NotImplementedError

    def find_median(self) -> float:
        raise NotImplementedError


if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    assert mf.find_median() == 1.0
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0
    mf = MedianFinder()
    for x in [5, -1, 3, 3, 10]:
        mf.add_num(x)
    assert mf.find_median() == 3.0
    mf.add_num(100)
    assert mf.find_median() == 4.0
    mf = MedianFinder()
    for x in range(10, 0, -1):
        mf.add_num(x)
    assert mf.find_median() == 5.5
    mf = MedianFinder()
    for x in [2, 2, 2]:
        mf.add_num(x)
    assert mf.find_median() == 2.0
    print("ok")
