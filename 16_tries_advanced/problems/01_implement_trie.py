"""
Problem: Implement Trie (Prefix Tree)
Difficulty: Medium | Pattern: Trie
Source: LeetCode 208

Implement a Trie with:
  insert(word)        -> stores the word
  search(word)        -> True if the exact word was inserted
  starts_with(prefix) -> True if any inserted word starts with prefix

Example:
  t = Trie(); t.insert("apple")
  t.search("apple") -> True; t.search("app") -> False; t.starts_with("app") -> True
  t.insert("app"); t.search("app") -> True

Hints:
1. Node = dict of children + end flag. `setdefault` makes insert a 3-liner.
2. Write one private walk(prefix) that returns the final node or None; search and
   starts_with both use it.
3. Empty string: starts_with("") is True; search("") is True only if "" was inserted.

Expected: O(L) time per operation for a word of length L, O(total characters) space
"""


class Trie:
    def __init__(self) -> None:
        raise NotImplementedError

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def starts_with(self, prefix: str) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.starts_with("app") is True
    t.insert("app")
    assert t.search("app") is True
    assert t.search("appl") is False
    assert t.starts_with("b") is False
    assert t.starts_with("") is True
    assert t.search("") is False
    t.insert("")
    assert t.search("") is True
    t.insert("apple")
    assert t.search("apple") is True
    print("ok")
