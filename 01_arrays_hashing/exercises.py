"""01 · Arrays & Hashing — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
"""
import random


def contains_duplicate(nums: list[int]) -> bool:
    """True if any value appears at least twice.
    [1, 2, 3, 1] -> True ; [1, 2, 3, 4] -> False
    """
    raise NotImplementedError


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices [i, j], i < j, with nums[i] + nums[j] == target. Exactly one answer exists.
    [2, 7, 11, 15], 9 -> [0, 1] ; [3, 2, 4], 6 -> [1, 2] ; [3, 3], 6 -> [0, 1]
    """
    raise NotImplementedError


def is_anagram(s: str, t: str) -> bool:
    """True if t is a rearrangement of s.
    "anagram", "nagaram" -> True ; "rat", "car" -> False
    """
    raise NotImplementedError


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other. Order of groups and within groups
    does not matter (the test sorts).
    ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    """
    raise NotImplementedError


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return the k most frequent values. Answer is unique; order does not matter.
    Aim for O(n) using buckets indexed by frequency. (A heap gives O(n log k); also fine.)
    [1,1,1,2,2,3], 2 -> [1, 2]
    """
    raise NotImplementedError


def product_except_self(nums: list[int]) -> list[int]:
    """out[i] = product of every element except nums[i]. No division. O(n).
    [1, 2, 3, 4] -> [24, 12, 8, 6] ; [-1, 1, 0, -3, 3] -> [0, 0, 9, 0, 0]
    """
    raise NotImplementedError


def max_subarray(nums: list[int]) -> int:
    """Largest sum of any non-empty contiguous subarray (Kadane).
    [-2,1,-3,4,-1,2,1,-5,4] -> 6  (the [4,-1,2,1]) ; [-3, -1, -2] -> -1
    """
    raise NotImplementedError


def subarray_sum_k(nums: list[int], k: int) -> int:
    """Count contiguous subarrays whose sum equals k. Numbers may be negative.
    [1, 1, 1], 2 -> 2 ; [1, 2, 3], 3 -> 2 ; [1, -1, 0], 0 -> 3
    """
    raise NotImplementedError


def longest_consecutive(nums: list[int]) -> int:
    """Length of the longest run of consecutive integers present (any order). O(n).
    [100, 4, 200, 1, 3, 2] -> 4  (1,2,3,4) ; [] -> 0
    """
    raise NotImplementedError


def encode(strs: list[str]) -> str:
    """Encode a list of strings into one string such that decode(encode(x)) == x.
    Strings may contain any character, including your delimiter and digits.
    """
    raise NotImplementedError


def decode(s: str) -> list[str]:
    """Inverse of encode."""
    raise NotImplementedError


class RandomizedSet:
    """insert / remove / get_random, each O(1) average.
    insert returns False if already present; remove returns False if absent.
    get_random returns a uniformly random present element.
    Hint: list of values + dict value -> index. Remove by swapping with the last element.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def insert(self, val: int) -> bool:
        raise NotImplementedError

    def remove(self, val: int) -> bool:
        raise NotImplementedError

    def get_random(self) -> int:
        raise NotImplementedError


def first_missing_positive(nums: list[int]) -> int:
    """Smallest positive integer not in nums. O(n) time, O(1) extra space.
    [1, 2, 0] -> 3 ; [3, 4, -1, 1] -> 2 ; [7, 8, 9] -> 1
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False


def _t_02_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


def _t_03_is_anagram():
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "ab") is False
    assert is_anagram("", "") is True


def _t_04_group_anagrams():
    got = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    norm = sorted(sorted(g) for g in got)
    assert norm == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]], norm
    assert group_anagrams([""]) == [[""]]


def _t_05_top_k_frequent():
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 5, 5, 6, 6, 6, 6], 2)) == [4, 6]


def _t_06_product_except_self():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([2, 3]) == [3, 2]


def _t_07_max_subarray():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([-3, -1, -2]) == -1
    assert max_subarray([5]) == 5
    assert max_subarray([1, 2, 3]) == 6


def _t_08_subarray_sum_k():
    assert subarray_sum_k([1, 1, 1], 2) == 2
    assert subarray_sum_k([1, 2, 3], 3) == 2
    assert subarray_sum_k([1, -1, 0], 0) == 3
    assert subarray_sum_k([1], 0) == 0


def _t_09_longest_consecutive():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([]) == 0
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([1, 1, 1]) == 1


def _t_10_encode_decode():
    for case in ([], [""], ["a"], ["hello", "world"], ["5#x", "#", "", "12", "a#b#c"]):
        assert decode(encode(case)) == case, case


def _t_11_randomized_set():
    rs = RandomizedSet()
    assert rs.insert(1) is True
    assert rs.remove(2) is False
    assert rs.insert(2) is True
    assert rs.get_random() in (1, 2)
    assert rs.remove(1) is True
    assert rs.insert(2) is False
    assert rs.get_random() == 2
    rs.insert(7); rs.insert(9); rs.remove(2)
    random.seed(0)
    seen = {rs.get_random() for _ in range(50)}
    assert seen == {7, 9}, seen


def _t_12_first_missing_positive():
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9]) == 1
    assert first_missing_positive([1]) == 2
    assert first_missing_positive([1, 1]) == 2


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
