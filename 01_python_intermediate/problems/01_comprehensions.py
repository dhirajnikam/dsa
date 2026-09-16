"""
Problem: Comprehensions
Difficulty: Warm-up | Topic: list/dict/set comprehensions, nested loops

Implement each function as a single comprehension (no explicit for loops).

1. squares_of_evens(nums): squares of the even numbers, in order. [1,2,3,4] -> [4, 16]
2. word_lengths(words): dict word -> len(word). ["hi", "hey"] -> {"hi": 2, "hey": 3}
3. first_letters(words): set of lowercase first letters of non-empty words.
   ["Apple", "avocado", "", "Bean"] -> {"a", "b"}
4. flatten(matrix): list of lists -> one list, row by row. [[1,2],[3]] -> [1,2,3]
5. transpose(matrix): rows become columns. [[1,2,3],[4,5,6]] -> [[1,4],[2,5],[3,6]]
   Assume a non-empty rectangular matrix.

Hints:
1. Filter goes at the end: [expr for x in xs if cond].
4. Two fors: [c for row in matrix for c in row]. Outer loop first.
5. [[row[j] for row in matrix] for j in range(len(matrix[0]))]
"""


def squares_of_evens(nums: list[int]) -> list[int]:
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    raise NotImplementedError


def first_letters(words: list[str]) -> set[str]:
    raise NotImplementedError


def flatten(matrix: list[list]) -> list:
    raise NotImplementedError


def transpose(matrix: list[list]) -> list[list]:
    raise NotImplementedError


if __name__ == "__main__":
    assert squares_of_evens([1, 2, 3, 4]) == [4, 16], 'Check: squares_of_evens([1, 2, 3, 4]) == [4, 16]'
    assert squares_of_evens([]) == [], 'Check: squares_of_evens([]) == []'
    assert squares_of_evens([-2, 0]) == [4, 0], 'Check: squares_of_evens([-2, 0]) == [4, 0]'
    assert word_lengths(["hi", "hey"]) == {"hi": 2, "hey": 3}, 'Check: word_lengths(["hi", "hey"]) == {"hi": 2, "hey": 3}'
    assert word_lengths([]) == {}, 'Check: word_lengths([]) == {}'
    assert first_letters(["Apple", "avocado", "", "Bean"]) == {"a", "b"}, 'Check: first_letters(["Apple", "avocado", "", "Bean"]) == {"a", "b"}'
    assert flatten([[1, 2], [3], []]) == [1, 2, 3], 'Check: flatten([[1, 2], [3], []]) == [1, 2, 3]'
    assert flatten([]) == [], 'Check: flatten([]) == []'
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], 'Check: transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]'
    assert transpose([[7]]) == [[7]], 'Check: transpose([[7]]) == [[7]]'
    print("ok")
