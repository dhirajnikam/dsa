"""
Problem: Longest Common Subsequence
Difficulty: Medium | Pattern: 2D DP on two strings
Source: LeetCode 1143

Return the length of the longest subsequence common to text1 and text2 (0 if none).

Example 1:
  text1 = "abcde", text2 = "ace" -> 3
Example 2:
  text1 = "abc", text2 = "abc" -> 3
Example 3:
  text1 = "abc", text2 = "def" -> 0

Constraints:
  1 <= len(text1), len(text2) <= 1000
  Lowercase letters only.

Hints:
1. State: dp[i][j] = LCS length of text1[:i] and text2[:j]. Row 0 and column 0 are 0.
2. Recurrence: if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1,
   else dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
3. Two rows of space are enough.

Expected: O(n * m) time, O(min(n, m)) space
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("a", "a") == 1
    assert longest_common_subsequence("a", "b") == 0
    assert longest_common_subsequence("bl", "yby") == 1
    assert longest_common_subsequence("ezupkr", "ubmrapg") == 2
    assert longest_common_subsequence("oxcpqrsvwf", "shmtulqrypy") == 2
    assert longest_common_subsequence("a" * 1000, "a" * 1000) == 1000
    print("ok")
