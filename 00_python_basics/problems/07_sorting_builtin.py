"""
Problem: Sorting with keys
Difficulty: Warm-up | Topic: sorted(), key=, lambda, stability

1. sort_by_length(["ccc", "a", "bb", "dd"]) -> ["a", "bb", "dd", "ccc"]  (stable: ties keep input order)
2. sort_people([("bob", 25), ("amy", 30), ("cat", 25)]) -> by age asc, then name asc
   -> [("bob", 25), ("cat", 25), ("amy", 30)]
3. top_k_frequent_words(["a","b","a","c","b","a"], 2) -> ["a", "b"]  (freq desc, then alphabetical)
4. sort_by_parity([3, 1, 2, 4]) -> evens first (in original order), then odds (in original order)
   -> [2, 4, 3, 1]

Hints:
2. key=lambda p: (p[1], p[0])
3. Count with a dict, then sorted(counts, key=lambda w: (-counts[w], w))[:k]
4. key=lambda x: x % 2 (False/0 sorts before True/1; sort is stable)
"""


def sort_by_length(words: list[str]) -> list[str]:
    raise NotImplementedError


def sort_people(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    raise NotImplementedError


def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    raise NotImplementedError


def sort_by_parity(nums: list[int]) -> list[int]:
    raise NotImplementedError


if __name__ == "__main__":
    assert sort_by_length(["ccc", "a", "bb", "dd"]) == ["a", "bb", "dd", "ccc"], 'Check: sort_by_length(["ccc", "a", "bb", "dd"]) == ["a", "bb", "dd", "ccc"]'
    assert sort_people([("bob", 25), ("amy", 30), ("cat", 25)]) == [("bob", 25), ("cat", 25), ("amy", 30)], 'Check: sort_people([("bob", 25), ("amy", 30), ("cat", 25)]) == [("bob", 25), ("cat", 25), ("amy", 30)]'
    assert top_k_frequent_words(["a", "b", "a", "c", "b", "a"], 2) == ["a", "b"], 'Check: top_k_frequent_words(["a", "b", "a", "c", "b", "a"], 2) == ["a", "b"]'
    assert top_k_frequent_words(["x", "y"], 1) == ["x"], 'Check: top_k_frequent_words(["x", "y"], 1) == ["x"]'
    assert sort_by_parity([3, 1, 2, 4]) == [2, 4, 3, 1], 'Check: sort_by_parity([3, 1, 2, 4]) == [2, 4, 3, 1]'
    print("ok")
