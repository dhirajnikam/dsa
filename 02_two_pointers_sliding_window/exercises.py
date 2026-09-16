"""02 · Two Pointers & Sliding Window — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
"""


def valid_palindrome(s: str) -> bool:
    """True if s reads the same both ways after dropping non-alphanumerics and ignoring case.
    O(1) extra space: two pointers on the original string, no cleaned copy.
    "A man, a plan, a canal: Panama" -> True ; "race a car" -> False ; " " -> True
    """
    raise NotImplementedError


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """nums is sorted ascending. Return 1-based indices [i, j], i < j, with nums[i-1] + nums[j-1]
    == target. Exactly one answer exists. O(1) extra space.
    [2, 7, 11, 15], 9 -> [1, 2] ; [2, 3, 4], 6 -> [1, 3] ; [-1, 0], -1 -> [1, 2]
    """
    raise NotImplementedError


def remove_duplicates_sorted(nums: list[int]) -> int:
    """nums is sorted. Remove duplicates in place so each value appears once, keeping order.
    Return the new length k; the first k slots of nums must hold the result.
    [1, 1, 2] -> 2 (nums starts [1, 2]) ; [0,0,1,1,1,2,2,3,3,4] -> 5 (nums starts [0,1,2,3,4])
    """
    raise NotImplementedError


def best_time_stock(prices: list[int]) -> int:
    """prices[i] is the price on day i. Buy once, sell once later. Maximum profit, or 0.
    [7, 1, 5, 3, 6, 4] -> 5 (buy 1, sell 6) ; [7, 6, 4, 3, 1] -> 0
    """
    raise NotImplementedError


def three_sum(nums: list[int]) -> list[list[int]]:
    """All unique triplets [a, b, c] from nums (distinct positions) with a + b + c == 0.
    Order of triplets and within a triplet does not matter (the test sorts).
    [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]] ; [0, 1, 1] -> [] ; [0, 0, 0] -> [[0, 0, 0]]
    """
    raise NotImplementedError


def container_most_water(height: list[int]) -> int:
    """Vertical lines of the given heights at x = 0, 1, 2, ... Pick two that hold the most
    water: area = (distance apart) * (shorter height). Return that area.
    [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49 ; [1, 1] -> 1
    """
    raise NotImplementedError


def longest_substring_no_repeat(s: str) -> int:
    """Length of the longest substring with all distinct characters.
    "abcabcbb" -> 3 ("abc") ; "bbbbb" -> 1 ; "pwwkew" -> 3 ("wke") ; "" -> 0
    """
    raise NotImplementedError


def longest_repeating_char_replacement(s: str, k: int) -> int:
    """s is uppercase letters. You may change at most k characters to any letter. Length of the
    longest substring that can be made all one letter.
    "ABAB", 2 -> 4 ; "AABABBA", 1 -> 4 ; "AAAA", 0 -> 4
    """
    raise NotImplementedError


def check_permutation_in_string(s1: str, s2: str) -> bool:
    """True if some permutation of s1 appears as a contiguous substring of s2. Lowercase letters.
    "ab", "eidbaooo" -> True ("ba") ; "ab", "eidboaoo" -> False ; "a", "a" -> True
    """
    raise NotImplementedError


def min_window_substring(s: str, t: str) -> str:
    """Shortest substring of s that contains every character of t, with multiplicity.
    Return "" if none. The answer is unique.
    "ADOBECODEBANC", "ABC" -> "BANC" ; "a", "a" -> "a" ; "a", "aa" -> ""
    """
    raise NotImplementedError


def trapping_rain_water(height: list[int]) -> int:
    """height[i] is the height of bar i (width 1). Total units of water trapped after rain.
    O(n) time, O(1) extra space with two pointers.
    [0,1,0,2,1,0,1,3,2,1,2,1] -> 6 ; [4, 2, 0, 3, 2, 5] -> 9 ; [2, 1] -> 0
    """
    raise NotImplementedError


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    """Maximum of every contiguous window of size k, left to right. O(n) with a monotonic deque.
    [1, 3, -1, -3, 5, 3, 6, 7], 3 -> [3, 3, 5, 5, 6, 7] ; [1], 1 -> [1]
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_valid_palindrome():
    assert valid_palindrome("A man, a plan, a canal: Panama") is True
    assert valid_palindrome("race a car") is False
    assert valid_palindrome(" ") is True
    assert valid_palindrome("0P") is False
    assert valid_palindrome(".,") is True


def _t_02_two_sum_sorted():
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]
    assert two_sum_sorted([-1, 0], -1) == [1, 2]
    assert two_sum_sorted([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]


def _t_03_remove_duplicates_sorted():
    a = [1, 1, 2]
    k = remove_duplicates_sorted(a)
    assert k == 2 and a[:k] == [1, 2], (k, a)
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates_sorted(a)
    assert k == 5 and a[:k] == [0, 1, 2, 3, 4], (k, a)
    a = [7]
    assert remove_duplicates_sorted(a) == 1 and a[:1] == [7]
    a = [3, 3, 3]
    assert remove_duplicates_sorted(a) == 1 and a[:1] == [3]


def _t_04_best_time_stock():
    assert best_time_stock([7, 1, 5, 3, 6, 4]) == 5
    assert best_time_stock([7, 6, 4, 3, 1]) == 0
    assert best_time_stock([5]) == 0
    assert best_time_stock([2, 4, 1, 7]) == 6


def _t_05_three_sum():
    def norm(ts):
        return sorted(sorted(t) for t in ts)
    assert norm(three_sum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert norm(three_sum([0, 0, 0])) == [[0, 0, 0]]
    assert norm(three_sum([0, 0, 0, 0])) == [[0, 0, 0]]
    assert norm(three_sum([-2, 0, 1, 1, 2])) == [[-2, 0, 2], [-2, 1, 1]]


def _t_06_container_most_water():
    assert container_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert container_most_water([1, 1]) == 1
    assert container_most_water([4, 3, 2, 1, 4]) == 16
    assert container_most_water([1, 2, 1]) == 2


def _t_07_longest_substring_no_repeat():
    assert longest_substring_no_repeat("abcabcbb") == 3
    assert longest_substring_no_repeat("bbbbb") == 1
    assert longest_substring_no_repeat("pwwkew") == 3
    assert longest_substring_no_repeat("") == 0
    assert longest_substring_no_repeat("abba") == 2


def _t_08_longest_repeating_char_replacement():
    assert longest_repeating_char_replacement("ABAB", 2) == 4
    assert longest_repeating_char_replacement("AABABBA", 1) == 4
    assert longest_repeating_char_replacement("AAAA", 0) == 4
    assert longest_repeating_char_replacement("ABCDE", 1) == 2
    assert longest_repeating_char_replacement("A", 5) == 1


def _t_09_check_permutation_in_string():
    assert check_permutation_in_string("ab", "eidbaooo") is True
    assert check_permutation_in_string("ab", "eidboaoo") is False
    assert check_permutation_in_string("a", "a") is True
    assert check_permutation_in_string("abc", "ab") is False
    assert check_permutation_in_string("adc", "dcda") is True


def _t_10_min_window_substring():
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window_substring("a", "a") == "a"
    assert min_window_substring("a", "aa") == ""
    assert min_window_substring("aa", "aa") == "aa"
    assert min_window_substring("abc", "b") == "b"


def _t_11_trapping_rain_water():
    assert trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trapping_rain_water([4, 2, 0, 3, 2, 5]) == 9
    assert trapping_rain_water([2, 1]) == 0
    assert trapping_rain_water([]) == 0
    assert trapping_rain_water([3, 0, 3]) == 3


def _t_12_sliding_window_maximum():
    assert sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_maximum([1], 1) == [1]
    assert sliding_window_maximum([9, 8, 7, 6], 2) == [9, 8, 7]
    assert sliding_window_maximum([1, 2, 3, 4], 4) == [4]
    assert sliding_window_maximum([4, 4, 4], 2) == [4, 4]


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
