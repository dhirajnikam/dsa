"""
Problem: Evaluate Reverse Polish Notation
Difficulty: Medium | Pattern: operand stack
Source: LeetCode 150

Evaluate an arithmetic expression in Reverse Polish Notation (postfix). Valid operators are
+, -, *, /. Each operand is an integer or another expression. Division truncates toward zero.
No division by zero occurs. The result and all intermediates fit in a 32-bit integer.

Example 1:
  tokens = ["2", "1", "+", "3", "*"] -> 9        ((2 + 1) * 3)
Example 2:
  tokens = ["4", "13", "5", "/", "+"] -> 6       (4 + (13 / 5))
Example 3:
  tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"] -> 22

Constraints:
  1 <= len(tokens) <= 10^4
  tokens are operators or integers in [-200, 200]

Hints:
1. Push numbers. On an operator, pop b then a (order matters for - and /), push a op b.
2. Python's // floors toward negative infinity; -7 // 2 == -4. You need truncation: int(a / b) gives -3.
3. "-11" is a number, not the minus operator. Check `token in "+-*/"` only for length-1 tokens, or use a dict of operators.

Expected: O(n) time, O(n) space
"""


def eval_rpn(tokens: list[str]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert eval_rpn(["18"]) == 18
    assert eval_rpn(["-7", "2", "/"]) == -3
    assert eval_rpn(["7", "-2", "/"]) == -3
    assert eval_rpn(["3", "4", "-"]) == -1
    assert eval_rpn(["0", "5", "*"]) == 0
    assert eval_rpn(["-3", "-4", "*"]) == 12
    print("ok")
