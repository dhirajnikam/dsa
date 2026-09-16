"""
Problem: Isomorphic Strings
Difficulty: Easy | Pattern: bijective mapping with two dicts
Source: LeetCode 205 (same idea as LeetCode 290 Word Pattern)

Two strings s and t are isomorphic if the characters in s can be replaced to get t.
Every occurrence of a character must map to the same character, no two characters may map
to the same character, and a character may map to itself.

Example 1:
  s = "egg", t = "add" -> True     (e->a, g->d)
Example 2:
  s = "foo", t = "bar" -> False    (o would need to map to both a and r)
Example 3:
  s = "paper", t = "title" -> True
Example 4:
  s = "badc", t = "baba" -> False  (a and c would both map to b)

Constraints:
  1 <= len(s) <= 5 * 10^4
  len(t) == len(s)
  any printable ASCII

Hints:
1. One dict s->t catches "one char maps to two things" but not "two chars map to one thing".
2. Keep two dicts (s->t and t->s) and check both directions at every position.
3. Slick alternative: compare the "first index of each char" fingerprints: [s.index(c) for c in s] == [t.index(c) for c in t].

Expected: O(n) time, O(1) space (bounded alphabet)
"""


def is_isomorphic(s: str, t: str) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert is_isomorphic("egg", "add") is True, 'Check: is_isomorphic("egg", "add") is True'
    assert is_isomorphic("foo", "bar") is False, 'Check: is_isomorphic("foo", "bar") is False'
    assert is_isomorphic("paper", "title") is True, 'Check: is_isomorphic("paper", "title") is True'
    assert is_isomorphic("badc", "baba") is False, 'Check: is_isomorphic("badc", "baba") is False'
    assert is_isomorphic("a", "a") is True, 'Check: is_isomorphic("a", "a") is True'
    assert is_isomorphic("a", "b") is True, 'Check: is_isomorphic("a", "b") is True'
    assert is_isomorphic("ab", "aa") is False, 'Check: is_isomorphic("ab", "aa") is False'
    assert is_isomorphic("aa", "ab") is False, 'Check: is_isomorphic("aa", "ab") is False'
    assert is_isomorphic("abcabc", "xyzxyz") is True, 'Check: is_isomorphic("abcabc", "xyzxyz") is True'
    print("ok")
