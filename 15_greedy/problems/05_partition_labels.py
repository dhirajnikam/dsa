"""
Problem: Partition Labels
Difficulty: Medium | Pattern: Greedy (extend to last occurrence)
Source: LeetCode 763

Given a string s of lowercase letters, partition it into as many parts as possible so that
each letter appears in at most one part. Return the sizes of the parts in order.

Example 1: s = "ababcbacadefegdehijhklij" -> [9, 7, 8]
Example 2: s = "eccbbbbdec" -> [10]

Hints:
1. Record last[c] = last index of each character.
2. Walk i with a current `end` = max(end, last[s[i]]). When i == end, close a part.
3. The partition is forced: a part must extend at least to the last occurrence of every
   letter inside it, and stopping as early as allowed maximises the count.

Expected: O(n) time, O(1) space (26 letters)
"""


def partition_labels(s: str) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8], 'Check: partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]'
    assert partition_labels("eccbbbbdec") == [10], 'Check: partition_labels("eccbbbbdec") == [10]'
    assert partition_labels("a") == [1], 'Check: partition_labels("a") == [1]'
    assert partition_labels("abc") == [1, 1, 1], 'Check: partition_labels("abc") == [1, 1, 1]'
    assert partition_labels("abca") == [4], 'Check: partition_labels("abca") == [4]'
    assert partition_labels("aabb") == [2, 2], 'Check: partition_labels("aabb") == [2, 2]'
    assert partition_labels("caedbdedda") == [1, 9], 'Check: partition_labels("caedbdedda") == [1, 9]'
    print("ok")
