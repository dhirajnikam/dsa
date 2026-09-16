"""
Problem: Valid Anagram
Difficulty: Easy | Pattern: frequency map comparison
Source: LeetCode 242

Given two strings s and t, return True if t is an anagram of s (same letters, same counts,
any order).

Example 1:
  s = "anagram", t = "nagaram" -> True
Example 2:
  s = "rat", t = "car" -> False

Constraints:
  0 <= len(s), len(t) <= 5 * 10^4
  lowercase English letters

Hints:
1. Different lengths can never be anagrams; check that first.
2. sorted(s) == sorted(t) works in O(n log n).
3. collections.Counter(s) == Counter(t) is O(n). Or one dict: +1 for s, -1 for t, all zero at the end.

Expected: O(n) time, O(1) space (alphabet is fixed size)
"""


def is_anagram(s: str, t: str) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True, 'Check: is_anagram("anagram", "nagaram") is True'
    assert is_anagram("rat", "car") is False, 'Check: is_anagram("rat", "car") is False'
    assert is_anagram("", "") is True, 'Check: is_anagram("", "") is True'
    assert is_anagram("a", "a") is True, 'Check: is_anagram("a", "a") is True'
    assert is_anagram("a", "ab") is False, 'Check: is_anagram("a", "ab") is False'
    assert is_anagram("aab", "abb") is False, 'Check: is_anagram("aab", "abb") is False'
    assert is_anagram("listen", "silent") is True, 'Check: is_anagram("listen", "silent") is True'
    assert is_anagram("aaaa", "aaaa") is True, 'Check: is_anagram("aaaa", "aaaa") is True'
    print("ok")
