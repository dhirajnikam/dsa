"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium | Pattern: variable window, shrink while invalid
Source: LeetCode 3

Given a string s, find the length of the longest substring with no repeated characters.

Example 1:
  s = "abcabcbb" -> 3   ("abc")
Example 2:
  s = "bbbbb" -> 1
Example 3:
  s = "pwwkew" -> 3     ("wke"; "pwke" is a subsequence, not a substring)

Constraints:
  0 <= len(s) <= 5 * 10^4
  letters, digits, symbols, spaces

Hints:
1. Window [l, r] must contain distinct characters. Track them in a set.
2. Expand r one step. While s[r] is already in the set, remove s[l] and l += 1. Then add s[r].
3. Faster: dict char -> last index; jump l straight to last[ch] + 1 if that is bigger than l.

Expected: O(n) time, O(min(n, alphabet)) space
"""


def length_of_longest_substring(s: str) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    assert length_of_longest_substring("au") == 2
    assert length_of_longest_substring("abba") == 2
    assert length_of_longest_substring("dvdf") == 3
    assert length_of_longest_substring("tmmzuxt") == 5
    print("ok")
