"""
Problem: Counting and grouping with collections
Difficulty: Easy | Topic: Counter, defaultdict, most_common, sorting with ties
Source: LeetCode 49, 242, 692 (variants)

1. top_k_words(words, k) -> k most frequent words, most frequent first, ties alphabetical.
2. group_anagrams(words) -> list of groups (lists) of words that are anagrams of each other.
   Groups in order of first appearance; words inside a group keep input order.
   ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]
3. missing_letters(word, magazine) -> Counter of letters needed by `word` that `magazine`
   does not supply enough of. missing_letters("aab", "ab") -> Counter({"a": 1}).
   Empty Counter when the magazine suffices.
4. first_unique_char(s) -> index of the first character that appears exactly once, or -1.
5. group_by_length(words) -> dict length -> sorted list of distinct words of that length.

Hints:
1. sorted(Counter(words).items(), key=lambda kv: (-kv[1], kv[0]))[:k]
2. Key an anagram group by "".join(sorted(w)) (or tuple of 26 counts) in a defaultdict(list).
3. Counter(word) - Counter(magazine) already drops non-positive counts.
"""
from collections import Counter, defaultdict


def top_k_words(words: list[str], k: int) -> list[str]:
    raise NotImplementedError


def group_anagrams(words: list[str]) -> list[list[str]]:
    raise NotImplementedError


def missing_letters(word: str, magazine: str) -> Counter:
    raise NotImplementedError


def first_unique_char(s: str) -> int:
    raise NotImplementedError


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    raise NotImplementedError


if __name__ == "__main__":
    assert top_k_words(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"], 'Check: top_k_words(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]'
    assert top_k_words(["b", "a", "c"], 2) == ["a", "b"], 'Check: top_k_words(["b", "a", "c"], 2) == ["a", "b"]'
    assert top_k_words([], 3) == [], 'Check: top_k_words([], 3) == []'
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["eat", "tea", "ate"], ["tan", "nat"], ["bat"]], 'Check: group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [ ["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]'
    assert group_anagrams([""]) == [[""]] and group_anagrams([]) == [], 'Check: group_anagrams([""]) == [[""]] and group_anagrams([]) == []'
    assert missing_letters("aab", "ab") == Counter({"a": 1}), 'Check: missing_letters("aab", "ab") == Counter({"a": 1})'
    assert missing_letters("abc", "cba") == Counter(), 'Check: missing_letters("abc", "cba") == Counter()'
    assert missing_letters("zz", "") == Counter({"z": 2}), 'Check: missing_letters("zz", "") == Counter({"z": 2})'
    assert first_unique_char("leetcode") == 0, 'Check: first_unique_char("leetcode") == 0'
    assert first_unique_char("loveleetcode") == 2, 'Check: first_unique_char("loveleetcode") == 2'
    assert first_unique_char("aabb") == -1 and first_unique_char("") == -1, 'Check: first_unique_char("aabb") == -1 and first_unique_char("") == -1'
    assert group_by_length(["a", "bb", "c", "dd", "a"]) == {1: ["a", "c"], 2: ["bb", "dd"]}, 'Check: group_by_length(["a", "bb", "c", "dd", "a"]) == {1: ["a", "c"], 2: ["bb", "dd"]}'
    assert group_by_length([]) == {}, 'Check: group_by_length([]) == {}'
    print("ok")
