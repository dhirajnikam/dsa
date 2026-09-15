"""
Problem: String Compression
Difficulty: Medium | Pattern: read/write pointers, in-place run-length encoding
Source: LeetCode 443

Given a list of characters chars, compress it IN PLACE using run-length encoding:
for each group of consecutive repeating characters, write the character, then the group
length if it is greater than 1 (lengths of 10 or more become multiple digit characters).
Return the new length k; the first k slots of chars must hold the compressed result.

Example 1:
  chars = ["a","a","b","b","c","c","c"] -> 6, chars[:6] = ["a","2","b","2","c","3"]
Example 2:
  chars = ["a"] -> 1, chars[:1] = ["a"]
Example 3:
  chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"] -> 4, chars[:4] = ["a","b","1","2"]

Constraints:
  1 <= len(chars) <= 2000
  letters, digits, and symbols

Hints:
1. Use a read pointer that finds the end of the current run and a write pointer that lags behind.
2. The write position never overtakes the read position, so overwriting is safe.
3. Write the count with `for d in str(count): chars[w] = d; w += 1`.

Expected: O(n) time, O(1) space
"""


def compress(chars: list[str]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    c = ["a", "a", "b", "b", "c", "c", "c"]
    k = compress(c)
    assert k == 6 and c[:k] == ["a", "2", "b", "2", "c", "3"]
    c = ["a"]
    k = compress(c)
    assert k == 1 and c[:k] == ["a"]
    c = ["a"] + ["b"] * 12
    k = compress(c)
    assert k == 4 and c[:k] == ["a", "b", "1", "2"]
    c = ["a", "b", "c"]
    k = compress(c)
    assert k == 3 and c[:k] == ["a", "b", "c"]
    c = ["z"] * 100
    k = compress(c)
    assert k == 4 and c[:k] == ["z", "1", "0", "0"]
    c = ["a", "a", "a", "b", "a"]
    k = compress(c)
    assert k == 4 and c[:k] == ["a", "3", "b", "a"]
    print("ok")
