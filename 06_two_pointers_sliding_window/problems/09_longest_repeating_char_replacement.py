"""
Problem: Longest Repeating Character Replacement
Difficulty: Medium | Pattern: variable window with Counter, validity = len - max_freq <= k
Source: LeetCode 424

You are given a string s of uppercase letters and an integer k. You may change at most k
characters to any other uppercase letter. Return the length of the longest substring that
can be made of a single repeated letter.

Example 1:
  s = "ABAB", k = 2 -> 4      (change both A's or both B's)
Example 2:
  s = "AABABBA", k = 1 -> 4   ("AABA" -> "AAAA")

Constraints:
  1 <= len(s) <= 10^5
  0 <= k <= len(s)
  uppercase English letters only

Hints:
1. A window is fixable iff (window length) - (count of its most frequent letter) <= k.
2. Expand r, update counts. While the window is not fixable, remove s[l], l += 1.
3. Optimisation: max_freq never needs to decrease (a shorter window with lower max can't beat
   the best you already recorded). Either version passes.

Expected: O(n) time, O(1) space (26 letters)
"""


def character_replacement(s: str, k: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4, 'Check: character_replacement("ABAB", 2) == 4'
    assert character_replacement("AABABBA", 1) == 4, 'Check: character_replacement("AABABBA", 1) == 4'
    assert character_replacement("A", 0) == 1, 'Check: character_replacement("A", 0) == 1'
    assert character_replacement("AAAA", 0) == 4, 'Check: character_replacement("AAAA", 0) == 4'
    assert character_replacement("ABCD", 0) == 1, 'Check: character_replacement("ABCD", 0) == 1'
    assert character_replacement("ABCD", 3) == 4, 'Check: character_replacement("ABCD", 3) == 4'
    assert character_replacement("ABBB", 2) == 4, 'Check: character_replacement("ABBB", 2) == 4'
    assert character_replacement("BAAAB", 2) == 5, 'Check: character_replacement("BAAAB", 2) == 5'
    assert character_replacement("ABCDE", 1) == 2, 'Check: character_replacement("ABCDE", 1) == 2'
    print("ok")
