"""
Problem: Valid Parentheses
Difficulty: Easy | Pattern: stack of open brackets
Source: LeetCode 20

Given a string s containing only the characters '(', ')', '{', '}', '[' and ']', determine
if the input is valid: every open bracket is closed by the same type, in the correct order,
and every close bracket has a matching open bracket.

Example 1:
  s = "()[]{}" -> True
Example 2:
  s = "(]" -> False
Example 3:
  s = "([)]" -> False
Example 4:
  s = "{[]}" -> True

Constraints:
  0 <= len(s) <= 10^4

Hints:
1. The most recently opened bracket must be the first one closed. That is LIFO: a stack.
2. Push opens. On a close, the stack must be non-empty and its top must be the matching open.
3. Valid iff the stack is empty at the end. A dict close -> open keeps the code short.

Expected: O(n) time, O(n) space
"""


def is_valid(s: str) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("") is True
    assert is_valid("(") is False
    assert is_valid(")") is False
    assert is_valid("((()))") is True
    assert is_valid("(()") is False
    assert is_valid("]]") is False
    print("ok")
