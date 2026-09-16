"""
Problem: Palindrome Partitioning
Difficulty: Medium | Pattern: Backtracking over cut positions
Source: LeetCode 131

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitionings of s, in any order.

Example 1:
  Input: s = "aab"
  Output: [["a","a","b"],["aa","b"]]

Example 2:
  Input: s = "a"
  Output: [["a"]]

Constraints:
  1 <= len(s) <= 16
  s contains only lowercase English letters.

Hints:
1. dfs(start): choose an end index; if s[start:end] is a palindrome, take it and recurse from end.
2. Base case: start == len(s) means the whole string is consumed; record the path.
3. A palindrome check is s[i:j] == s[i:j][::-1]. For speed, precompute a 2D table (optional).

Expected: O(n * 2^n) time, O(n) extra space.
"""


def partition(s: str) -> list[list[str]]:
    raise NotImplementedError


if __name__ == "__main__":
    assert sorted(partition("aab")) == [["a", "a", "b"], ["aa", "b"]], 'Check: sorted(partition("aab")) == [["a", "a", "b"], ["aa", "b"]]'
    assert partition("a") == [["a"]], 'Check: partition("a") == [["a"]]'
    assert sorted(partition("ab")) == [["a", "b"]], 'Check: sorted(partition("ab")) == [["a", "b"]]'
    assert sorted(partition("aaa")) == [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]], 'Check: sorted(partition("aaa")) == [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]'
    out = partition("abba")
    assert sorted(out) == [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]], 'Check: sorted(out) == [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]'
    assert all("".join(p) == "abcba" for p in partition("abcba")), 'Check: all("".join(p) == "abcba" for p in partition("abcba"))'
    assert len(partition("aaaaaaaa")) == 128, 'Check: len(partition("aaaaaaaa")) == 128'   # every cut set works: 2^(n-1)
    print("ok")
