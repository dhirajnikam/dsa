"""
Problem: Alien Dictionary
Difficulty: Hard | Pattern: build graph from constraints + topological sort
Source: LeetCode 269

You are given a list of words sorted lexicographically by the rules of an unknown alien
language that uses lowercase letters. Return a string of the unique letters in the
language, sorted by the alien order. If the order is invalid, return "". If several
orders are valid, return any one of them.

Rules of the order: for two adjacent words, the first position where they differ tells
you letter_a < letter_b. If a word is a prefix of the next word that is fine; if a longer
word comes BEFORE its own prefix ("abc" before "ab"), the input is invalid.

Example 1:
  words = ["wrt","wrf","er","ett","rftt"] -> "wertf"
Example 2:
  words = ["z","x"] -> "zx"
Example 3:
  words = ["z","x","z"] -> ""   (cycle)
Example 4:
  words = ["abc","ab"] -> ""    (prefix violation)

Constraints:
  1 <= len(words) <= 100
  1 <= len(words[i]) <= 100

Hints:
1. Every letter in every word is a node, even letters with no constraints.
2. For each adjacent pair, find the first differing char: edge a -> b. If none differs and
   the first word is longer, return "".
3. Kahn's algorithm. If the output is missing letters, there was a cycle: return "".

Expected: O(total characters) time, O(1) space (26 letters)
"""
from collections import defaultdict, deque


def alien_order(words: list[str]) -> str:
    raise NotImplementedError


if __name__ == "__main__":
    def valid(result, words):
        letters = {ch for w in words for ch in w}
        if set(result) != letters or len(result) != len(letters):
            return False
        pos = {ch: i for i, ch in enumerate(result)}
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if pos[x] > pos[y]:
                        return False
                    break
            else:
                if len(a) > len(b):
                    return False
        return True

    w = ["wrt", "wrf", "er", "ett", "rftt"]
    assert alien_order(w) == "wertf", 'Check: alien_order(w) == "wertf"'
    assert alien_order(["z", "x"]) == "zx", 'Check: alien_order(["z", "x"]) == "zx"'
    assert alien_order(["z", "x", "z"]) == "", 'Check: alien_order(["z", "x", "z"]) == ""'
    assert alien_order(["abc", "ab"]) == "", 'Check: alien_order(["abc", "ab"]) == ""'
    assert alien_order(["ab", "abc"]) in ("abc", "acb", "bac", "bca", "cab", "cba"), 'Check: alien_order(["ab", "abc"]) in ("abc", "acb", "bac", "bca", "cab", "cba")'
    assert valid(alien_order(["ab", "abc"]), ["ab", "abc"]), 'Check: valid(alien_order(["ab", "abc"]), ["ab", "abc"])'
    assert alien_order(["a"]) == "a", 'Check: alien_order(["a"]) == "a"'
    assert alien_order(["a", "a"]) == "a", 'Check: alien_order(["a", "a"]) == "a"'
    w = ["ac", "ab", "zc", "zb"]
    assert valid(alien_order(w), w), 'Check: valid(alien_order(w), w)'
    w = ["ba", "bc", "ac", "cab"]
    assert valid(alien_order(w), w), 'Check: valid(alien_order(w), w)'
    assert alien_order(["z", "z", "x", "z"]) == "", 'Check: alien_order(["z", "z", "x", "z"]) == ""'
    print("ok")
