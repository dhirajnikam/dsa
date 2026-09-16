"""
Problem: Edit Distance
Difficulty: Medium | Pattern: 2D DP on two strings, 3 operations
Source: LeetCode 72

Return the minimum number of operations (insert a character, delete a character, replace
a character) to convert word1 into word2.

Example 1:
  word1 = "horse", word2 = "ros" -> 3   (horse -> rorse -> rose -> ros)
Example 2:
  word1 = "intention", word2 = "execution" -> 5

Constraints:
  0 <= len(word1), len(word2) <= 500
  Lowercase letters only.

Hints:
1. State: dp[i][j] = edits to turn word1[:i] into word2[:j]. dp[i][0] = i, dp[0][j] = j.
2. Recurrence: if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1];
   else dp[i][j] = 1 + min(dp[i-1][j] (delete), dp[i][j-1] (insert), dp[i-1][j-1] (replace)).

Expected: O(n * m) time, O(m) space
"""


def min_distance(word1: str, word2: str) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3, 'Check: min_distance("horse", "ros") == 3'
    assert min_distance("intention", "execution") == 5, 'Check: min_distance("intention", "execution") == 5'
    assert min_distance("", "") == 0, 'Check: min_distance("", "") == 0'
    assert min_distance("", "abc") == 3, 'Check: min_distance("", "abc") == 3'
    assert min_distance("abc", "") == 3, 'Check: min_distance("abc", "") == 3'
    assert min_distance("abc", "abc") == 0, 'Check: min_distance("abc", "abc") == 0'
    assert min_distance("a", "b") == 1, 'Check: min_distance("a", "b") == 1'
    assert min_distance("kitten", "sitting") == 3, 'Check: min_distance("kitten", "sitting") == 3'
    assert min_distance("zoologicoarchaeologist", "zoogeologist") == 10, 'Check: min_distance("zoologicoarchaeologist", "zoogeologist") == 10'
    print("ok")
