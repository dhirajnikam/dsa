"""
Problem: Valid Palindrome
Difficulty: Easy | Pattern: opposite-direction two pointers
Source: LeetCode 125

A phrase is a palindrome if, after converting uppercase to lowercase and removing all
non-alphanumeric characters, it reads the same forwards and backwards.
Given a string s, return True if it is a palindrome.

Example 1:
  s = "A man, a plan, a canal: Panama" -> True   ("amanaplanacanalpanama")
Example 2:
  s = "race a car" -> False
Example 3:
  s = " " -> True   (empty after cleaning)

Constraints:
  1 <= len(s) <= 2 * 10^5
  printable ASCII

Hints:
1. Easy version: build the cleaned string and compare with its reverse. O(n) extra space.
2. Two pointers l, r from both ends. Skip non-alphanumerics with str.isalnum(). Compare lowered chars.
3. Stop when l >= r.

Expected: O(n) time, O(1) space
"""


def is_palindrome(s: str) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("ab@ba") is True
    assert is_palindrome("aa") is True
    assert is_palindrome(".,") is True
    print("ok")
