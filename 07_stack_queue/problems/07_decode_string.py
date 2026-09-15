"""
Problem: Decode String
Difficulty: Medium | Pattern: stack of (prefix, repeat count) frames for nested parsing
Source: LeetCode 394

Given an encoded string, return its decoded string. The encoding rule is k[encoded_string],
meaning encoded_string inside the brackets is repeated exactly k times. k is a positive integer.
The input is always valid; digits appear only as repeat counts. Nesting is allowed.

Example 1:
  s = "3[a]2[bc]" -> "aaabcbc"
Example 2:
  s = "3[a2[c]]" -> "accaccacc"
Example 3:
  s = "2[abc]3[cd]ef" -> "abcabccdcdcdef"

Constraints:
  1 <= len(s) <= 30
  lowercase letters, digits, and square brackets
  1 <= k <= 300; output length <= 10^5

Hints:
1. Walk the string keeping `cur` (the string being built) and `num` (the count being read).
2. On '[': push (cur, num) to the stack, reset both. On ']': pop (prev, k); cur = prev + cur * k.
3. Multi-digit counts: num = num * 10 + int(ch). Letters append to cur.

Expected: O(output length) time, O(nesting depth + output) space
"""


def decode_string(s: str) -> str:
    raise NotImplementedError


if __name__ == "__main__":
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert decode_string("abc") == "abc"
    assert decode_string("1[x]") == "x"
    assert decode_string("10[a]") == "a" * 10
    assert decode_string("2[2[2[z]]]") == "z" * 8
    assert decode_string("a2[b3[c]d]e") == "abcccdbcccde"
    assert decode_string("0[a]b") == "b"
    print("ok")
