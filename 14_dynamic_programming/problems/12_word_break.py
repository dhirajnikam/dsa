"""
Problem: Word Break
Difficulty: Medium | Pattern: 1D DP over string positions
Source: LeetCode 139

Given a string s and a list of words wordDict, return True if s can be segmented into a
space-separated sequence of one or more dictionary words (words may be reused).

Example 1:
  s = "leetcode", wordDict = ["leet", "code"] -> True
Example 2:
  s = "applepenapple", wordDict = ["apple", "pen"] -> True
Example 3:
  s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"] -> False

Constraints:
  1 <= len(s) <= 300
  1 <= len(wordDict) <= 1000, 1 <= len(word) <= 20, all words distinct

Hints:
1. State: dp[i] = can s[:i] be segmented. dp[0] = True.
2. Recurrence: dp[i] = any(dp[j] and s[j:i] in words for j < i). Put words in a set.
3. Speed-up: only try j = i - len(w) for lengths that exist in the dictionary.

Expected: O(n^2 * L) time, O(n) space   (L = max word length for slicing)
"""


def word_break(s: str, word_dict: list[str]) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"]) is True, 'Check: word_break("leetcode", ["leet", "code"]) is True'
    assert word_break("applepenapple", ["apple", "pen"]) is True, 'Check: word_break("applepenapple", ["apple", "pen"]) is True'
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False, 'Check: word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False'
    assert word_break("a", ["a"]) is True, 'Check: word_break("a", ["a"]) is True'
    assert word_break("a", ["b"]) is False, 'Check: word_break("a", ["b"]) is False'
    assert word_break("aaaaaaa", ["aaaa", "aaa"]) is True, 'Check: word_break("aaaaaaa", ["aaaa", "aaa"]) is True'
    assert word_break("aaaaaaa", ["aaaa", "aa"]) is False, 'Check: word_break("aaaaaaa", ["aaaa", "aa"]) is False'
    assert word_break("cars", ["car", "ca", "rs"]) is True, 'Check: word_break("cars", ["car", "ca", "rs"]) is True'
    assert word_break("a" * 300, ["a" * 20, "b"]) is True, 'Check: word_break("a" * 300, ["a" * 20, "b"]) is True'
    assert word_break("a" * 299, ["a" * 20, "a" * 30]) is False, 'Check: word_break("a" * 299, ["a" * 20, "a" * 30]) is False'
    print("ok")
