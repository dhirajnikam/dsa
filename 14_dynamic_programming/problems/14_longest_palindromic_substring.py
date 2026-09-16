"""
Problem: Longest Palindromic Substring
Difficulty: Medium | Pattern: expand around center / 2D palindrome table
Source: LeetCode 5

Return the longest palindromic substring of s. If several have the maximum length,
return the one that starts first.

Example 1:
  s = "babad" -> "bab"   ("aba" also has length 3 but starts later)
Example 2:
  s = "cbbd" -> "bb"

Constraints:
  1 <= len(s) <= 1000
  Letters and digits.

Hints:
1. DP state: is_pal[i][j] = s[i:j+1] is a palindrome.
   Recurrence: is_pal[i][j] = s[i] == s[j] and (j - i < 2 or is_pal[i+1][j-1]). Fill by length.
2. Same O(n^2) with O(1) space: for each center (i, i) and (i, i+1), expand while the ends match.
3. Track (start, length) of the best; with ties, only update when strictly longer.

Expected: O(n^2) time, O(1) space (expand) or O(n^2) space (table)
"""


def longest_palindrome(s: str) -> str:
    raise NotImplementedError


if __name__ == "__main__":
    assert longest_palindrome("babad") == "bab", 'Check: longest_palindrome("babad") == "bab"'
    assert longest_palindrome("cbbd") == "bb", 'Check: longest_palindrome("cbbd") == "bb"'
    assert longest_palindrome("a") == "a", 'Check: longest_palindrome("a") == "a"'
    assert longest_palindrome("ac") == "a", 'Check: longest_palindrome("ac") == "a"'
    assert longest_palindrome("aaaa") == "aaaa", 'Check: longest_palindrome("aaaa") == "aaaa"'
    assert longest_palindrome("racecar") == "racecar", 'Check: longest_palindrome("racecar") == "racecar"'
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg", 'Check: longest_palindrome("forgeeksskeegfor") == "geeksskeeg"'
    assert longest_palindrome("abcda") == "a", 'Check: longest_palindrome("abcda") == "a"'
    assert longest_palindrome("abb") == "bb", 'Check: longest_palindrome("abb") == "bb"'
    assert longest_palindrome("a" * 1000) == "a" * 1000, 'Check: longest_palindrome("a" * 1000) == "a" * 1000'
    print("ok")
