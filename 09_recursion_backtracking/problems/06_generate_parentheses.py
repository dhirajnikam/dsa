"""
Problem: Generate Parentheses
Difficulty: Medium | Pattern: Backtracking with validity pruning
Source: LeetCode 22

Given n pairs of parentheses, generate all combinations of well-formed parentheses.

Example 1:
  Input: n = 3
  Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
  Input: n = 1
  Output: ["()"]

Constraints:
  1 <= n <= 8

Hints:
1. Track how many '(' and ')' have been placed. You may add '(' while open < n.
2. You may add ')' only while close < open, otherwise the string is invalid.
3. Record when the string has length 2n. Pruning makes this generate only valid strings.

Expected: O(4^n / sqrt(n)) time (Catalan number of outputs), O(n) extra space.
"""


def generate_parenthesis(n: int) -> list[str]:
    raise NotImplementedError


if __name__ == "__main__":
    assert sorted(generate_parenthesis(3)) == ["((()))", "(()())", "(())()", "()(())", "()()()"], 'Check: sorted(generate_parenthesis(3)) == ["((()))", "(()())", "(())()", "()(())", "()()()"]'
    assert generate_parenthesis(1) == ["()"], 'Check: generate_parenthesis(1) == ["()"]'
    assert sorted(generate_parenthesis(2)) == ["(())", "()()"], 'Check: sorted(generate_parenthesis(2)) == ["(())", "()()"]'
    assert generate_parenthesis(0) == [""], 'Check: generate_parenthesis(0) == [""]'
    out = generate_parenthesis(5)
    assert len(out) == 42 and len(set(out)) == 42, 'Check: len(out) == 42 and len(set(out)) == 42'   # Catalan(5)
    assert len(generate_parenthesis(8)) == 1430, 'Check: len(generate_parenthesis(8)) == 1430'
    print("ok")
