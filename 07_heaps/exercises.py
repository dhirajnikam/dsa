"""07 · Heaps — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
"""
import heapq  # noqa: F401 — you will want this
from collections import Counter  # noqa: F401 — and this


class KthLargest:
    """Stream version of kth largest. __init__ receives k and the initial numbers; every
    add(val) inserts val and returns the kth largest value seen so far. Duplicates count.
    KthLargest(3, [4, 5, 8, 2]); add(3) -> 4; add(5) -> 5; add(10) -> 5; add(9) -> 8; add(4) -> 8
    """

    def __init__(self, k: int, nums: list[int]) -> None:
        raise NotImplementedError

    def add(self, val: int) -> int:
        raise NotImplementedError


def kth_largest(nums: list[int], k: int) -> int:
    """The kth largest element in sorted order (duplicates count). 1 <= k <= len(nums).
    Aim for O(n log k) with a heap; read about quickselect in solutions.py afterwards.
    [3, 2, 1, 5, 6, 4], 2 -> 5 ; [3, 2, 3, 1, 2, 4, 5, 5, 6], 4 -> 4 ; [1], 1 -> 1
    """
    raise NotImplementedError


def last_stone_weight(stones: list[int]) -> int:
    """Repeatedly smash the two heaviest stones: if equal both vanish, otherwise the heavier
    becomes their difference. Return the weight of the last stone, or 0 if none remain.
    [2, 7, 4, 1, 8, 1] -> 1 ; [1] -> 1 ; [2, 2] -> 0
    """
    raise NotImplementedError


def k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    """The k points closest to the origin by Euclidean distance. Answer is unique as a set;
    order does not matter (the test sorts). Aim for O(n log k).
    [[1, 3], [-2, 2]], 1 -> [[-2, 2]] ; [[3, 3], [5, -1], [-2, 4]], 2 -> [[3, 3], [-2, 4]]
    """
    raise NotImplementedError


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    """The k most frequent values, using a heap of size k for O(n log k). Answer is unique;
    order does not matter. (Chapter 01 did this with buckets in O(n).)
    [1, 1, 1, 2, 2, 3], 2 -> [1, 2] ; [1], 1 -> [1]
    """
    raise NotImplementedError


def task_scheduler(tasks: list[str], n: int) -> int:
    """Each task takes one unit of time. The same task must be separated by at least n
    units (you may idle). Return the least total time to run everything.
    ["A","A","A","B","B","B"], 2 -> 8  (A B _ A B _ A B) ; ["A","A","A","B","B","B"], 0 -> 6 ;
    ["A","A","A","A","A","A","B","C","D","E","F","G"], 2 -> 16
    """
    raise NotImplementedError


class MedianFinder:
    """add_num(x) adds a value; find_median() returns the median of everything added so far
    (mean of the two middle values when the count is even). Both O(log n) / O(1).
    add 1, add 2 -> find_median() == 1.5 ; add 3 -> find_median() == 2.0
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def add_num(self, num: int) -> None:
        raise NotImplementedError

    def find_median(self) -> float:
        raise NotImplementedError


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    """Merge k sorted lists into one sorted list in O(N log k), N = total elements.
    Hint: heap of (value, list_index, element_index).
    [[1, 4, 5], [1, 3, 4], [2, 6]] -> [1, 1, 2, 3, 4, 4, 5, 6] ; [] -> [] ; [[]] -> []
    """
    raise NotImplementedError


def reorganize_string(s: str) -> str:
    """Rearrange s so that no two adjacent characters are equal. Return any valid
    arrangement, or "" if none exists. The test checks the property, not an exact string.
    "aab" -> "aba" ; "aaab" -> "" ; "a" -> "a"
    """
    raise NotImplementedError


def meeting_rooms_ii(intervals: list[list[int]]) -> int:
    """Minimum number of rooms so that no two overlapping meetings share a room.
    A meeting ending at t and another starting at t do not overlap.
    [[0, 30], [5, 10], [15, 20]] -> 2 ; [[7, 10], [2, 4]] -> 1 ; [] -> 0
    """
    raise NotImplementedError


def kth_smallest_in_sorted_matrix(matrix: list[list[int]], k: int) -> int:
    """The kth smallest value in an n x n matrix whose rows and columns are each sorted
    ascending. Values may repeat. Aim for O(k log n).
    [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8 -> 13 ; [[-5]], 1 -> -5
    """
    raise NotImplementedError


def smallest_range_covering_k_lists(lists: list[list[int]]) -> list[int]:
    """Smallest [a, b] that contains at least one number from each of the k sorted lists.
    Smaller b - a wins; ties go to the smaller a.
    [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]] -> [20, 24] ; [[1, 2, 3], [1, 2, 3]] -> [1, 1]
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_kth_largest_stream():
    kl = KthLargest(3, [4, 5, 8, 2])
    assert kl.add(3) == 4
    assert kl.add(5) == 5
    assert kl.add(10) == 5
    assert kl.add(9) == 8
    assert kl.add(4) == 8
    kl2 = KthLargest(1, [])              # fewer initial numbers than k
    assert kl2.add(-3) == -3
    assert kl2.add(-2) == -2
    assert kl2.add(-4) == -2


def _t_02_kth_largest():
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert kth_largest([1], 1) == 1
    assert kth_largest([7, 7, 7], 2) == 7
    assert kth_largest([5, -1, 3], 3) == -1


def _t_03_last_stone_weight():
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1
    assert last_stone_weight([1]) == 1
    assert last_stone_weight([2, 2]) == 0
    assert last_stone_weight([10, 4, 2, 10]) == 2
    assert last_stone_weight([]) == 0


def _t_04_k_closest_points():
    assert sorted(k_closest_points([[1, 3], [-2, 2]], 1)) == [[-2, 2]]
    assert sorted(k_closest_points([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]
    assert sorted(k_closest_points([[0, 0]], 1)) == [[0, 0]]
    got = k_closest_points([[1, 1], [2, 2], [3, 3], [-1, 0]], 4)
    assert sorted(got) == [[-1, 0], [1, 1], [2, 2], [3, 3]]


def _t_05_top_k_frequent_heap():
    assert sorted(top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent_heap([1], 1) == [1]
    assert sorted(top_k_frequent_heap([4, 4, 4, 5, 5, 6, 6, 6, 6], 2)) == [4, 6]
    assert sorted(top_k_frequent_heap([1, 2, 3], 3)) == [1, 2, 3]


def _t_06_task_scheduler():
    assert task_scheduler(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert task_scheduler(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert task_scheduler(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
    assert task_scheduler(["A"], 5) == 1
    assert task_scheduler(["A", "A", "B"], 3) == 5           # A B _ _ A


def _t_07_median_finder():
    mf = MedianFinder()
    mf.add_num(1)
    assert mf.find_median() == 1.0
    mf.add_num(2)
    assert mf.find_median() == 1.5
    mf.add_num(3)
    assert mf.find_median() == 2.0
    mf2 = MedianFinder()
    for x in [5, -1, 100, 0, 7, 7]:
        mf2.add_num(x)
    assert mf2.find_median() == 6.0                           # sorted: -1 0 5 7 7 100
    mf2.add_num(-50)
    assert mf2.find_median() == 5.0


def _t_08_merge_k_sorted():
    assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_sorted([]) == []
    assert merge_k_sorted([[]]) == []
    assert merge_k_sorted([[], [1], []]) == [1]
    assert merge_k_sorted([[3], [1], [2]]) == [1, 2, 3]


def _valid_reorg(original: str, got: str) -> bool:
    return (sorted(original) == sorted(got)
            and all(got[i] != got[i + 1] for i in range(len(got) - 1)))


def _t_09_reorganize_string():
    assert _valid_reorg("aab", reorganize_string("aab"))
    assert reorganize_string("aaab") == ""
    assert reorganize_string("a") == "a"
    assert _valid_reorg("vvvlo", reorganize_string("vvvlo"))
    assert _valid_reorg("aaabbc", reorganize_string("aaabbc"))
    assert _valid_reorg("abab", reorganize_string("abab"))


def _t_10_meeting_rooms_ii():
    assert meeting_rooms_ii([[0, 30], [5, 10], [15, 20]]) == 2
    assert meeting_rooms_ii([[7, 10], [2, 4]]) == 1
    assert meeting_rooms_ii([]) == 0
    assert meeting_rooms_ii([[1, 5], [5, 10]]) == 1                    # touching is fine
    assert meeting_rooms_ii([[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]) == 4


def _t_11_kth_smallest_in_sorted_matrix():
    assert kth_smallest_in_sorted_matrix([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13
    assert kth_smallest_in_sorted_matrix([[-5]], 1) == -5
    assert kth_smallest_in_sorted_matrix([[1, 2], [1, 3]], 2) == 1
    assert kth_smallest_in_sorted_matrix([[1, 2], [1, 3]], 4) == 3
    assert kth_smallest_in_sorted_matrix([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 1) == 1


def _t_12_smallest_range_covering_k_lists():
    assert smallest_range_covering_k_lists(
        [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]) == [20, 24]
    assert smallest_range_covering_k_lists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == [1, 1]
    assert smallest_range_covering_k_lists([[7]]) == [7, 7]
    assert smallest_range_covering_k_lists([[1], [10]]) == [1, 10]
    assert smallest_range_covering_k_lists([[10, 10], [11, 11]]) == [10, 11]


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
