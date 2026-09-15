"""
Problem: Group Anagrams
Difficulty: Medium | Pattern: grouping by canonical key
Source: LeetCode 49

Given an array of strings strs, group the anagrams together. Return the groups in any order;
the strings within a group may be in any order.

Example 1:
  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
  -> [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
Example 2:
  strs = [""] -> [[""]]
Example 3:
  strs = ["a"] -> [["a"]]

Constraints:
  1 <= len(strs) <= 10^4
  0 <= len(strs[i]) <= 100
  lowercase English letters

Hints:
1. Two strings are anagrams iff they map to the same canonical form. What form?
2. "".join(sorted(word)) is a valid key. defaultdict(list) collects members.
3. O(k) key instead of O(k log k): a tuple of 26 letter counts (tuples are hashable; lists are not).

Expected: O(n * k log k) time (or O(n * k) with count keys), O(n * k) space
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    raise NotImplementedError


if __name__ == "__main__":
    def norm(groups):
        return sorted(sorted(g) for g in groups)

    assert norm(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert norm(group_anagrams([""])) == [[""]]
    assert norm(group_anagrams(["a"])) == [["a"]]
    assert norm(group_anagrams(["", ""])) == [["", ""]]
    assert norm(group_anagrams(["ab", "ba", "abc"])) == [["ab", "ba"], ["abc"]]
    assert norm(group_anagrams(["x", "y", "z"])) == [["x"], ["y"], ["z"]]
    assert norm(group_anagrams(["aa", "aa", "a"])) == [["a"], ["aa", "aa"]]
    print("ok")
