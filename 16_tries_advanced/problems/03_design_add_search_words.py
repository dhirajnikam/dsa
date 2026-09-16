"""
Problem: Design Add and Search Words Data Structure
Difficulty: Medium | Pattern: Trie with wildcard DFS
Source: LeetCode 211

Design a data structure supporting:
  add_word(word)  -> stores the word
  search(word)    -> True if any stored word matches; word may contain '.' which matches
                     exactly one letter of any kind

Example:
  d = WordDictionary(); d.add_word("bad"); d.add_word("dad"); d.add_word("mad")
  d.search("pad") -> False; d.search("bad") -> True; d.search(".ad") -> True; d.search("b..") -> True

Hints:
1. Same trie as 01. search is a recursive helper search_from(node, i).
2. On a '.', try every child; on a letter, follow that child only.
3. Match must consume the whole word AND land on an end marker: ".." must not match "bad".

Expected: O(L) add; search O(L) for plain words, O(26^dots * L) worst case with wildcards
"""


class WordDictionary:
    def __init__(self) -> None:
        raise NotImplementedError

    def add_word(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    d = WordDictionary()
    d.add_word("bad")
    d.add_word("dad")
    d.add_word("mad")
    assert d.search("pad") is False, 'Check: d.search("pad") is False'
    assert d.search("bad") is True, 'Check: d.search("bad") is True'
    assert d.search(".ad") is True, 'Check: d.search(".ad") is True'
    assert d.search("b..") is True, 'Check: d.search("b..") is True'
    assert d.search("...") is True, 'Check: d.search("...") is True'
    assert d.search("..") is False, 'Check: d.search("..") is False'
    assert d.search("....") is False, 'Check: d.search("....") is False'
    assert d.search("b.d") is True, 'Check: d.search("b.d") is True'
    assert d.search("") is False, 'Check: d.search("") is False'
    d.add_word("a")
    assert d.search(".") is True, 'Check: d.search(".") is True'
    assert d.search("a.") is False, 'Check: d.search("a.") is False'
    print("ok")
