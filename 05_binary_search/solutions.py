"""05 · Binary Search — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""
from bisect import bisect_right
from collections import defaultdict


def binary_search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1          # closed interval of live indices
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
    # O(log n) time, O(1) space.


def search_insert_position(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)              # half-open: first i with nums[i] >= target, or n
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo
    # O(log n). This is bisect_left.


def first_and_last_position(nums: list[int], target: int) -> list[int]:
    def first_true(pred) -> int:       # smallest i in [0, n) with pred(i), else n
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if pred(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    first = first_true(lambda i: nums[i] >= target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    last = first_true(lambda i: nums[i] > target) - 1
    return [first, last]
    # Two O(log n) searches. Same as bisect_left / bisect_right.


def search_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1              # treat the matrix as one sorted list of length m*n
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
    # O(log(m*n)) time, O(1) space.


def min_eating_speed(piles: list[int], h: int) -> int:
    def hours(k: int) -> int:
        return sum((p + k - 1) // k for p in piles)     # ceil(p / k) per pile

    lo, hi = 1, max(piles)             # speed max(piles) always finishes in len(piles) hours
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h:            # feasible: slower speeds are the only ones left to try
            hi = mid
        else:
            lo = mid + 1
    return lo
    # O(n log(max pile)). Monotone: a faster speed never needs more hours.


def find_min_rotated(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1          # find first i with nums[i] <= nums[-1]
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= nums[-1]:      # mid is in the second (smaller) sorted run
            hi = mid
        else:
            lo = mid + 1
    return nums[lo]
    # O(log n). The answer is always in range, so no sentinel needed.


def search_rotated(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:                       # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                           # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
    # O(log n). Distinct values make the "which half is sorted" test unambiguous.


class TimeMap:
    def __init__(self) -> None:
        self.times: dict[str, list[int]] = defaultdict(list)   # sorted, since sets increase
        self.values: dict[str, list[str]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)
        # O(1) amortized.

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        i = bisect_right(self.times[key], timestamp)   # count of stamps <= timestamp
        return self.values[key][i - 1] if i else ""
        # O(log k) for k versions of the key.


def ship_within_days(weights: list[int], days: int) -> int:
    def days_needed(cap: int) -> int:
        d, load = 1, 0
        for w in weights:
            if load + w > cap:         # greedy: start a new day only when forced
                d += 1
                load = 0
            load += w
        return d

    lo, hi = max(weights), sum(weights)   # cap below max never works; sum always works in 1 day
    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(mid) <= days:
            hi = mid
        else:
            lo = mid + 1
    return lo
    # O(n log(sum - max)). Monotone: more capacity never needs more days.


def split_array_largest_sum(nums: list[int], k: int) -> int:
    def pieces_needed(limit: int) -> int:
        count, running = 1, 0
        for x in nums:
            if running + x > limit:
                count += 1
                running = 0
            running += x
        return count

    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if pieces_needed(mid) <= k:    # fewer pieces than allowed is fine: split any piece further
            hi = mid
        else:
            lo = mid + 1
    return lo
    # Identical shape to ship_within_days. O(n log(sum)). The DP alternative is O(k n^2).


def median_two_sorted(a: list[int], b: list[int]) -> float:
    if len(a) > len(b):
        a, b = b, a                    # binary search over the shorter array
    m, n = len(a), len(b)
    half = (m + n + 1) // 2            # size of the left partition
    lo, hi = 0, m                      # i = how many of a go left; j = half - i from b
    INF = float("inf")
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        a_left = a[i - 1] if i > 0 else -INF
        a_right = a[i] if i < m else INF
        b_left = b[j - 1] if j > 0 else -INF
        b_right = b[j] if j < n else INF
        if a_left <= b_right and b_left <= a_right:     # valid partition
            if (m + n) % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            hi = i - 1                 # took too many from a
        else:
            lo = i + 1                 # took too few from a
    raise ValueError("inputs were not sorted")
    # O(log(min(m, n))) time, O(1) space.


def peak_element(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1          # find first i with nums[i] > nums[i+1]; i = n-1 if none
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid + 1]:  # descending here: a peak is at mid or to the left
            hi = mid
        else:
            lo = mid + 1               # ascending: a peak is strictly to the right
    return lo
    # O(log n). mid + 1 <= hi always holds because lo < hi, so no index error.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
