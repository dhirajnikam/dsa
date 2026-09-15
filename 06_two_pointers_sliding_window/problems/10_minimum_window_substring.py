"""
Problem: Minimum Window Substring
Difficulty: Hard | Pattern: variable window with Counter and "need/have" bookkeeping
Source: LeetCode 76

Given strings s and t, return the minimum window substring of s that contains every
character of t (including duplicates). If no such window exists return "".
The answer is guaranteed unique.

Example 1:
  s = "ADOBECODEBANC", t = "ABC" -> "BANC"
Example 2:
  s = "a", t = "a" -> "a"
Example 3:
  s = "a", t = "aa" -> ""

Constraints:
  1 <= len(s), len(t) <= 10^5
  uppercase and lowercase English letters

Hints:
1. need = Counter(t). Track how many DISTINCT characters currently have counts satisfied
   (have == len(need) means the window is valid).
2. Expand r. When window[ch] reaches need[ch], have += 1. While have == len(need): record the
   window if smaller, then remove s[l]; if that drops window[ch] below need[ch], have -= 1.
3. Store the best as (length, l, r) indices and slice once at the end. Do not build substrings inside the loop.

Expected: O(|s| + |t|) time, O(alphabet) space
"""


def min_window(s: str, t: str) -> str:
    raise NotImplementedError


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("ab", "b") == "b"
    assert min_window("aa", "aa") == "aa"
    assert min_window("abc", "cba") == "abc"
    assert min_window("xyz", "q") == ""
    assert min_window("aaflslflsldkalskaaa", "aaa") == "aaa"
    assert min_window("bba", "ab") == "ba"
    assert min_window("cabwefgewcwaefgcf", "cae") == "cwae"
    print("ok")
