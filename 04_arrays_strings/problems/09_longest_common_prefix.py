"""
Problem: Longest Common Prefix
Difficulty: Easy | Pattern: vertical scan / zip(*strs)
Source: LeetCode 14

Write a function that finds the longest common prefix string among an array of strings.
If there is none, return "".

Example 1:
  strs = ["flower", "flow", "flight"] -> "fl"
Example 2:
  strs = ["dog", "racecar", "car"] -> ""

Constraints:
  1 <= len(strs) <= 200
  0 <= len(strs[i]) <= 200
  lowercase English letters only

Hints:
1. Compare column by column: position 0 of every word, then position 1, ...; stop at the first mismatch.
2. zip(*strs) yields exactly those columns and stops at the shortest string.
3. Alternative: the common prefix of min(strs) and max(strs) (lexicographic) is the answer.

Expected: O(S) time where S = total characters, O(1) extra space
"""


def longest_common_prefix(strs: list[str]) -> str:
    raise NotImplementedError


if __name__ == "__main__":
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl", 'Check: longest_common_prefix(["flower", "flow", "flight"]) == "fl"'
    assert longest_common_prefix(["dog", "racecar", "car"]) == "", 'Check: longest_common_prefix(["dog", "racecar", "car"]) == ""'
    assert longest_common_prefix(["alone"]) == "alone", 'Check: longest_common_prefix(["alone"]) == "alone"'
    assert longest_common_prefix(["same", "same", "same"]) == "same", 'Check: longest_common_prefix(["same", "same", "same"]) == "same"'
    assert longest_common_prefix(["", "abc"]) == "", 'Check: longest_common_prefix(["", "abc"]) == ""'
    assert longest_common_prefix(["abc", "ab", "a"]) == "a", 'Check: longest_common_prefix(["abc", "ab", "a"]) == "a"'
    assert longest_common_prefix(["ab", "abc", "abcd"]) == "ab", 'Check: longest_common_prefix(["ab", "abc", "abcd"]) == "ab"'
    assert longest_common_prefix([""]) == "", 'Check: longest_common_prefix([""]) == ""'
    print("ok")
