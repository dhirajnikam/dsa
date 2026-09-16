"""10 · Dynamic Programming — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
For every problem, write the four lines first: state, transition, base case, answer location.
"""


def climbing_stairs(n: int) -> int:
    """Number of distinct ways to climb n steps taking 1 or 2 steps at a time. n >= 1.
    2 -> 2 ; 3 -> 3 ; 5 -> 8
    """
    raise NotImplementedError


def min_cost_climbing_stairs(cost: list[int]) -> int:
    """cost[i] is paid when you step on stair i. From stair i you may climb to i+1 or i+2.
    You may start on stair 0 or 1. The top is one past the last stair. Return the minimum
    total cost to reach the top. len(cost) >= 2.
    [10, 15, 20] -> 15 ; [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] -> 6
    """
    raise NotImplementedError


def house_robber(nums: list[int]) -> int:
    """Houses in a row hold nums[i] cash. You cannot rob two adjacent houses.
    Return the most cash you can take.
    [1, 2, 3, 1] -> 4 ; [2, 7, 9, 3, 1] -> 12 ; [] -> 0
    """
    raise NotImplementedError


def house_robber_ii(nums: list[int]) -> int:
    """Same as house_robber, but the houses form a circle: the first and last are adjacent.
    [2, 3, 2] -> 3 ; [1, 2, 3, 1] -> 4 ; [1] -> 1
    """
    raise NotImplementedError


def longest_palindromic_substring(s: str) -> str:
    """Return a longest substring of s that reads the same backward. Any valid answer is
    accepted when several have the maximum length. len(s) >= 1.
    "babad" -> "bab" or "aba" ; "cbbd" -> "bb" ; "a" -> "a"
    """
    raise NotImplementedError


def count_palindromic_substrings(s: str) -> int:
    """Count substrings of s that are palindromes. Different positions count separately.
    "abc" -> 3 ; "aaa" -> 6 ; "abba" -> 6
    """
    raise NotImplementedError


def decode_ways(s: str) -> int:
    """'A'..'Z' were encoded as "1".."26" and concatenated. Count the ways to decode s.
    A leading '0' in a piece is invalid ("06" is not 6).
    "12" -> 2 ("AB", "L") ; "226" -> 3 ; "06" -> 0
    """
    raise NotImplementedError


def coin_change(coins: list[int], amount: int) -> int:
    """Fewest coins (unlimited supply of each denomination) that sum to amount, or -1 if
    it cannot be done.
    [1, 2, 5], 11 -> 3 ; [2], 3 -> -1 ; [1], 0 -> 0
    """
    raise NotImplementedError


def coin_change_ii(coins: list[int], amount: int) -> int:
    """Number of distinct combinations of coins (unlimited supply) that sum to amount.
    Order does not matter: 1+2 and 2+1 are one combination.
    [1, 2, 5], 5 -> 4 ; [2], 3 -> 0 ; [10], 10 -> 1
    """
    raise NotImplementedError


def max_product_subarray(nums: list[int]) -> int:
    """Largest product of any non-empty contiguous subarray.
    [2, 3, -2, 4] -> 6 ; [-2, 0, -1] -> 0 ; [-2, 3, -4] -> 24
    """
    raise NotImplementedError


def word_break(s: str, words: list[str]) -> bool:
    """True if s can be split into a sequence of words from the list (reuse allowed).
    "leetcode", ["leet", "code"] -> True ; "applepenapple", ["apple", "pen"] -> True
    "catsandog", ["cats", "dog", "sand", "and", "cat"] -> False
    """
    raise NotImplementedError


def length_of_lis(nums: list[int]) -> int:
    """Length of the longest strictly increasing subsequence. Do O(n^2) first, then O(n log n).
    [10, 9, 2, 5, 3, 7, 101, 18] -> 4 ; [0, 1, 0, 3, 2, 3] -> 4 ; [7, 7, 7] -> 1
    """
    raise NotImplementedError


def can_partition(nums: list[int]) -> bool:
    """True if nums can be split into two groups with equal sums. All values positive.
    [1, 5, 11, 5] -> True ; [1, 2, 3, 5] -> False ; [1] -> False
    """
    raise NotImplementedError


def unique_paths(m: int, n: int) -> int:
    """Number of paths from the top-left to the bottom-right of an m x n grid moving only
    right or down.
    3, 7 -> 28 ; 3, 2 -> 3 ; 1, 1 -> 1
    """
    raise NotImplementedError


def longest_common_subsequence(s: str, t: str) -> int:
    """Length of the longest sequence of characters that appears in both s and t in order
    (not necessarily contiguous).
    "abcde", "ace" -> 3 ; "abc", "abc" -> 3 ; "abc", "def" -> 0
    """
    raise NotImplementedError


def edit_distance(s: str, t: str) -> int:
    """Minimum single-character insertions, deletions, or replacements to turn s into t.
    "horse", "ros" -> 3 ; "intention", "execution" -> 5 ; "", "abc" -> 3
    """
    raise NotImplementedError


def max_profit_with_cooldown(prices: list[int]) -> int:
    """prices[i] is a stock price on day i. Buy and sell as often as you like, holding at
    most one share, but after a sale you must skip one day before buying again.
    Return the maximum profit.
    [1, 2, 3, 0, 2] -> 3 ; [1] -> 0 ; [1, 2, 4] -> 3
    """
    raise NotImplementedError


def target_sum_ways(nums: list[int], target: int) -> int:
    """Put a '+' or '-' in front of every number so the expression equals target.
    Count the assignments. Values are non-negative.
    [1, 1, 1, 1, 1], 3 -> 5 ; [1], 1 -> 1 ; [1], 2 -> 0
    """
    raise NotImplementedError


def interleaving_string(s1: str, s2: str, s3: str) -> bool:
    """True if s3 can be formed by interleaving s1 and s2: split each into pieces and merge
    them alternately, keeping each string's pieces in order.
    "aabcc", "dbbca", "aadbbcbcac" -> True ; "aabcc", "dbbca", "aadbbbaccc" -> False
    "", "", "" -> True
    """
    raise NotImplementedError


def burst_balloons(nums: list[int]) -> int:
    """Balloon i is worth nums[i]. Bursting it earns nums[left] * nums[i] * nums[right] using
    its current neighbors (treat missing neighbors as 1), then the neighbors close ranks.
    Return the most coins you can earn bursting them all.
    [3, 1, 5, 8] -> 167 ; [1, 5] -> 10 ; [] -> 0
    """
    raise NotImplementedError


def regex_match(s: str, p: str) -> bool:
    """Pattern p uses '.' (any one character) and '*' (zero or more of the preceding element).
    True if p matches all of s.
    "aa", "a" -> False ; "aa", "a*" -> True ; "ab", ".*" -> True ; "aab", "c*a*b" -> True
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_climbing_stairs():
    assert climbing_stairs(1) == 1
    assert climbing_stairs(2) == 2
    assert climbing_stairs(3) == 3
    assert climbing_stairs(5) == 8
    assert climbing_stairs(45) == 1836311903


def _t_02_min_cost_climbing_stairs():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert min_cost_climbing_stairs([5, 10]) == 5
    assert min_cost_climbing_stairs([0, 0, 0, 0]) == 0


def _t_03_house_robber():
    assert house_robber([1, 2, 3, 1]) == 4
    assert house_robber([2, 7, 9, 3, 1]) == 12
    assert house_robber([]) == 0
    assert house_robber([5]) == 5
    assert house_robber([2, 1, 1, 2]) == 4


def _t_04_house_robber_ii():
    assert house_robber_ii([2, 3, 2]) == 3
    assert house_robber_ii([1, 2, 3, 1]) == 4
    assert house_robber_ii([1, 2, 3]) == 3
    assert house_robber_ii([1]) == 1
    assert house_robber_ii([]) == 0


def _t_05_longest_palindromic_substring():
    def ok(s, length):
        got = longest_palindromic_substring(s)
        assert got == got[::-1] and got in s and len(got) == length, (s, got)
    ok("babad", 3)
    ok("cbbd", 2)
    ok("a", 1)
    ok("ac", 1)
    ok("forgeeksskeegfor", 10)


def _t_06_count_palindromic_substrings():
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6
    assert count_palindromic_substrings("abba") == 6
    assert count_palindromic_substrings("a") == 1


def _t_07_decode_ways():
    assert decode_ways("12") == 2
    assert decode_ways("226") == 3
    assert decode_ways("06") == 0
    assert decode_ways("0") == 0
    assert decode_ways("10") == 1
    assert decode_ways("2101") == 1
    assert decode_ways("1111") == 5


def _t_08_coin_change():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([2, 5, 10, 1], 27) == 4
    assert coin_change([186, 419, 83, 408], 6249) == 20


def _t_09_coin_change_ii():
    assert coin_change_ii([1, 2, 5], 5) == 4
    assert coin_change_ii([2], 3) == 0
    assert coin_change_ii([10], 10) == 1
    assert coin_change_ii([1, 2, 3], 4) == 4
    assert coin_change_ii([3, 7], 0) == 1


def _t_10_max_product_subarray():
    assert max_product_subarray([2, 3, -2, 4]) == 6
    assert max_product_subarray([-2, 0, -1]) == 0
    assert max_product_subarray([-2]) == -2
    assert max_product_subarray([-2, 3, -4]) == 24
    assert max_product_subarray([-3, -1, -1]) == 3


def _t_11_word_break():
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert word_break("", ["a"]) is True
    assert word_break("aaaaaaa", ["aaaa", "aaa"]) is True


def _t_12_length_of_lis():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7]) == 1
    assert length_of_lis([]) == 0
    assert length_of_lis(list(range(3000))) == 3000
    assert length_of_lis(list(range(3000, 0, -1))) == 1


def _t_13_can_partition():
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
    assert can_partition([1, 1]) is True
    assert can_partition([1]) is False
    assert can_partition([100] * 20) is True


def _t_14_unique_paths():
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(1, 1) == 1
    assert unique_paths(1, 10) == 1
    assert unique_paths(10, 10) == 48620


def _t_15_longest_common_subsequence():
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("", "abc") == 0
    assert longest_common_subsequence("bsbininm", "jmjkbkjkv") == 1


def _t_16_edit_distance():
    assert edit_distance("horse", "ros") == 3
    assert edit_distance("intention", "execution") == 5
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "abc") == 0
    assert edit_distance("a", "b") == 1


def _t_17_max_profit_with_cooldown():
    assert max_profit_with_cooldown([1, 2, 3, 0, 2]) == 3
    assert max_profit_with_cooldown([1]) == 0
    assert max_profit_with_cooldown([]) == 0
    assert max_profit_with_cooldown([1, 2, 4]) == 3
    assert max_profit_with_cooldown([2, 1]) == 0
    assert max_profit_with_cooldown([6, 1, 3, 2, 4, 7]) == 6


def _t_18_target_sum_ways():
    assert target_sum_ways([1, 1, 1, 1, 1], 3) == 5
    assert target_sum_ways([1], 1) == 1
    assert target_sum_ways([1], 2) == 0
    assert target_sum_ways([2, 3], 1) == 1
    assert target_sum_ways([0, 0, 0, 0, 0, 0, 0, 0, 1], 1) == 256


def _t_19_interleaving_string():
    assert interleaving_string("aabcc", "dbbca", "aadbbcbcac") is True
    assert interleaving_string("aabcc", "dbbca", "aadbbbaccc") is False
    assert interleaving_string("", "", "") is True
    assert interleaving_string("a", "", "a") is True
    assert interleaving_string("a", "b", "ab") is True
    assert interleaving_string("abc", "def", "abcdefg") is False


def _t_20_burst_balloons():
    assert burst_balloons([3, 1, 5, 8]) == 167
    assert burst_balloons([1, 5]) == 10
    assert burst_balloons([]) == 0
    assert burst_balloons([5]) == 5
    assert burst_balloons([1, 2, 3]) == 12


def _t_21_regex_match():
    assert regex_match("aa", "a") is False
    assert regex_match("aa", "a*") is True
    assert regex_match("ab", ".*") is True
    assert regex_match("aab", "c*a*b") is True
    assert regex_match("mississippi", "mis*is*p*.") is False
    assert regex_match("", "a*") is True
    assert regex_match("", "") is True
    assert regex_match("ab", ".*c") is False


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
