"""
Problem: Dict and set basics
Difficulty: Warm-up | Topic: hash maps, counting, membership

1. char_frequency("banana") -> {"b": 1, "a": 3, "n": 2}
2. first_unique_char("leetcode") -> 0 ; "loveleetcode" -> 2 ; "aabb" -> -1   (LeetCode 387)
3. common_elements([1, 2, 2, 3], [2, 2, 3, 4]) -> [2, 3]  sorted, no duplicates
4. invert_dict({"a": 1, "b": 2}) -> {1: "a", 2: "b"}

Hints:
1. d[c] = d.get(c, 0) + 1
2. Count first, then scan the string in order for the first count == 1.
3. Set intersection, then sorted().
"""


def char_frequency(s: str) -> dict:
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    return count


def first_unique_char(s: str) -> int:
    count = char_frequency(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1
    




def common_elements(a: list, b: list) -> list:
    return sorted(set(a) & set(b))






def invert_dict(d: dict) -> dict:
    inv = {}
    for key, value in d.items():
        inv[value] = key 
    return inv




if __name__ == "__main__":
    assert char_frequency("banana") == {"b": 1, "a": 3, "n": 2}
    assert char_frequency("") == {}
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert common_elements([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3]
    assert common_elements([], [1]) == []
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    print("ok")
