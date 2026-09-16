"""05 · Binary Search — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
"""


def binary_search(nums: list[int], target: int) -> int:
    """Index of target in a sorted array of distinct ints, or -1. O(log n).
    [-1, 0, 3, 5, 9, 12], 9 -> 4 ; [-1, 0, 3, 5, 9, 12], 2 -> -1 ; [], 1 -> -1
    """
    raise NotImplementedError


def search_insert_position(nums: list[int], target: int) -> int:
    """Index of target in a sorted array of distinct ints, or the index where it would be
    inserted to keep the array sorted. O(log n).
    [1, 3, 5, 6], 5 -> 2 ; [1, 3, 5, 6], 2 -> 1 ; [1, 3, 5, 6], 7 -> 4
    """
    raise NotImplementedError


def first_and_last_position(nums: list[int], target: int) -> list[int]:
    """[first index, last index] of target in a sorted array that may have duplicates.
    [-1, -1] if target is absent. O(log n).
    [5, 7, 7, 8, 8, 10], 8 -> [3, 4] ; [5, 7, 7, 8, 8, 10], 6 -> [-1, -1] ; [], 0 -> [-1, -1]
    """
    raise NotImplementedError


def search_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    """True if target is in the matrix. Each row is sorted, and the first value of every
    row is greater than the last value of the row above it. O(log(m * n)).
    [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3 -> True ; same, 13 -> False
    """
    raise NotImplementedError


def min_eating_speed(piles: list[int], h: int) -> int:
    """Koko eats bananas at speed k per hour; each hour she picks one pile and eats k from it
    (a pile smaller than k still takes the whole hour). Return the minimum integer k that
    finishes every pile within h hours. h >= len(piles).
    [3, 6, 7, 11], 8 -> 4 ; [30, 11, 23, 4, 20], 5 -> 30 ; [30, 11, 23, 4, 20], 6 -> 23
    """
    raise NotImplementedError


def find_min_rotated(nums: list[int]) -> int:
    """Minimum of a sorted array of distinct ints that was rotated some number of times.
    O(log n).
    [3, 4, 5, 1, 2] -> 1 ; [4, 5, 6, 7, 0, 1, 2] -> 0 ; [11, 13, 15, 17] -> 11
    """
    raise NotImplementedError


def search_rotated(nums: list[int], target: int) -> int:
    """Index of target in a rotated sorted array of distinct ints, or -1. O(log n).
    [4, 5, 6, 7, 0, 1, 2], 0 -> 4 ; [4, 5, 6, 7, 0, 1, 2], 3 -> -1 ; [1], 0 -> -1
    """
    raise NotImplementedError


class TimeMap:
    """Key-value store where every value carries a timestamp.
    set(key, value, timestamp): store the value. Timestamps for a given key strictly increase
      across calls.
    get(key, timestamp): the value stored with the largest timestamp <= the given one,
      or "" if there is none.
    set("foo", "bar", 1); get("foo", 1) -> "bar"; get("foo", 3) -> "bar";
    set("foo", "bar2", 4); get("foo", 4) -> "bar2"; get("foo", 5) -> "bar2"; get("x", 1) -> ""
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def set(self, key: str, value: str, timestamp: int) -> None:
        raise NotImplementedError

    def get(self, key: str, timestamp: int) -> str:
        raise NotImplementedError


def ship_within_days(weights: list[int], days: int) -> int:
    """Packages must ship in the given order, one contiguous batch per day, and no day may
    exceed the ship's capacity. Return the minimum capacity that ships everything in
    `days` days.
    [1,2,3,4,5,6,7,8,9,10], 5 -> 15 ; [3, 2, 2, 4, 1, 4], 3 -> 6 ; [1, 2, 3, 1, 1], 4 -> 3
    """
    raise NotImplementedError


def split_array_largest_sum(nums: list[int], k: int) -> int:
    """Split nums into k non-empty contiguous subarrays so that the largest subarray sum is
    as small as possible. Return that minimized largest sum.
    [7, 2, 5, 10, 8], 2 -> 18 ; [1, 2, 3, 4, 5], 2 -> 9 ; [1, 4, 4], 3 -> 4
    """
    raise NotImplementedError


def median_two_sorted(a: list[int], b: list[int]) -> float:
    """Median of the merged sorted arrays a and b, in O(log(min(m, n))) time.
    At least one of the arrays is non-empty.
    [1, 3], [2] -> 2.0 ; [1, 2], [3, 4] -> 2.5 ; [], [1] -> 1.0
    """
    raise NotImplementedError


def peak_element(nums: list[int]) -> int:
    """Index of any element strictly greater than both neighbours. Treat nums[-1] and
    nums[n] as negative infinity. Adjacent values are never equal. O(log n).
    [1, 2, 3, 1] -> 2 ; [1, 2, 1, 3, 5, 6, 4] -> 1 or 5 ; [1] -> 0
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_binary_search():
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([], 1) == -1
    assert binary_search([1, 2], 1) == 0 and binary_search([1, 2], 2) == 1


def _t_02_search_insert_position():
    assert search_insert_position([1, 3, 5, 6], 5) == 2
    assert search_insert_position([1, 3, 5, 6], 2) == 1
    assert search_insert_position([1, 3, 5, 6], 7) == 4
    assert search_insert_position([1, 3, 5, 6], 0) == 0
    assert search_insert_position([], 3) == 0


def _t_03_first_and_last_position():
    assert first_and_last_position([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert first_and_last_position([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert first_and_last_position([], 0) == [-1, -1]
    assert first_and_last_position([2, 2, 2, 2], 2) == [0, 3]
    assert first_and_last_position([1, 2, 3], 3) == [2, 2]


def _t_04_search_2d_matrix():
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_2d_matrix(m, 3) is True
    assert search_2d_matrix(m, 13) is False
    assert search_2d_matrix(m, 60) is True and search_2d_matrix(m, 1) is True
    assert search_2d_matrix([[1]], 2) is False
    assert search_2d_matrix([[1], [3]], 3) is True


def _t_05_min_eating_speed():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    assert min_eating_speed([1], 1) == 1
    assert min_eating_speed([1000000000], 2) == 500000000


def _t_06_find_min_rotated():
    assert find_min_rotated([3, 4, 5, 1, 2]) == 1
    assert find_min_rotated([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min_rotated([11, 13, 15, 17]) == 11
    assert find_min_rotated([1]) == 1
    assert find_min_rotated([2, 1]) == 1


def _t_07_search_rotated():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    assert search_rotated([1], 1) == 0
    assert search_rotated([5, 1, 3], 5) == 0
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 7) == 3


def _t_08_time_map():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"
    assert tm.get("foo", 0) == ""
    assert tm.get("missing", 10) == ""


def _t_09_ship_within_days():
    assert ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert ship_within_days([3, 2, 2, 4, 1, 4], 3) == 6
    assert ship_within_days([1, 2, 3, 1, 1], 4) == 3
    assert ship_within_days([10], 1) == 10
    assert ship_within_days([1, 1, 1, 1], 4) == 1


def _t_10_split_array_largest_sum():
    assert split_array_largest_sum([7, 2, 5, 10, 8], 2) == 18
    assert split_array_largest_sum([1, 2, 3, 4, 5], 2) == 9
    assert split_array_largest_sum([1, 4, 4], 3) == 4
    assert split_array_largest_sum([5], 1) == 5
    assert split_array_largest_sum([2, 3, 1, 2, 4, 3], 6) == 4


def _t_11_median_two_sorted():
    assert median_two_sorted([1, 3], [2]) == 2.0
    assert median_two_sorted([1, 2], [3, 4]) == 2.5
    assert median_two_sorted([], [1]) == 1.0
    assert median_two_sorted([2], []) == 2.0
    assert median_two_sorted([1, 2, 3, 4, 5, 6], [7]) == 4.0
    assert median_two_sorted([1, 1], [1, 1]) == 1.0


def _t_12_peak_element():
    assert peak_element([1, 2, 3, 1]) == 2
    assert peak_element([1, 2, 1, 3, 5, 6, 4]) in (1, 5)
    assert peak_element([1]) == 0
    assert peak_element([1, 2]) == 1
    assert peak_element([2, 1]) == 0


def _check():
    checks = [(n[3:], f) for n, f in sorted(globals().items()) if n.startswith("_t_")]
    passed = 0
    for name, fn in checks:
        try:
            fn()
            print(f"PASS  {name}")
            passed += 1
        except NotImplementedError:
            print(f"TODO  {name}")
        except AssertionError as e:
            print(f"FAIL  {name}  {e}")
        except Exception as e:  # noqa: BLE001 — show the student what blew up
            print(f"FAIL  {name}  {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(checks)} passed")


if __name__ == "__main__":
    _check()
