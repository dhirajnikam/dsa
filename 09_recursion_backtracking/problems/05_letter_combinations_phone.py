"""
Problem: Letter Combinations of a Phone Number
Difficulty: Medium | Pattern: Backtracking (cartesian product)
Source: LeetCode 17

Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent, in any order. Mapping is the classic phone keypad:
  2: abc  3: def  4: ghi  5: jkl  6: mno  7: pqrs  8: tuv  9: wxyz

Example 1:
  Input: digits = "23"
  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
  Input: digits = ""
  Output: []

Example 3:
  Input: digits = "2"
  Output: ["a","b","c"]

Constraints:
  0 <= len(digits) <= 4
  digits[i] is in '2'..'9'

Hints:
1. Position i in the output picks one letter from the mapping of digits[i]. Depth = len(digits).
2. When index == len(digits), join the path and record it.
3. Empty input is a special case: return [] not [""].

Expected: O(4^n * n) time, O(n) extra space.
"""


def letter_combinations(digits: str) -> list[str]:
    raise NotImplementedError


if __name__ == "__main__":
    assert sorted(letter_combinations("23")) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], 'Check: sorted(letter_combinations("23")) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]'
    assert letter_combinations("") == [], 'Check: letter_combinations("") == []'
    assert sorted(letter_combinations("2")) == ["a", "b", "c"], 'Check: sorted(letter_combinations("2")) == ["a", "b", "c"]'
    assert sorted(letter_combinations("7")) == ["p", "q", "r", "s"], 'Check: sorted(letter_combinations("7")) == ["p", "q", "r", "s"]'
    out = letter_combinations("79")
    assert len(out) == 16 and len(set(out)) == 16 and all(len(s) == 2 for s in out), 'Check: len(out) == 16 and len(set(out)) == 16 and all(len(s) == 2 for s in out)'
    assert len(letter_combinations("2345")) == 81, 'Check: len(letter_combinations("2345")) == 81'
    print("ok")
