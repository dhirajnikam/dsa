"""
Problem: Decode Ways
Difficulty: Medium | Pattern: 1D DP with validity rules
Source: LeetCode 91

Letters A-Z are encoded as 1-26. Given a digit string s, return the number of ways to
decode it. "0" cannot stand alone, and two-digit groups must be 10..26 ("06" is invalid).

Example 1:
  s = "12" -> 2   (AB, L)
Example 2:
  s = "226" -> 3   (BZ, VF, BBF)
Example 3:
  s = "06" -> 0

Constraints:
  1 <= len(s) <= 100
  Digits only, may contain leading zeros.

Hints:
1. State: dp[i] = ways to decode s[:i]. dp[0] = 1 (empty prefix).
2. Recurrence: dp[i] = (dp[i-1] if s[i-1] != '0') + (dp[i-2] if 10 <= int(s[i-2:i]) <= 26).
3. Two rolling variables; return 0 early when dp hits 0 twice in a row if you like.

Expected: O(n) time, O(1) space
"""


def num_decodings(s: str) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert num_decodings("12") == 2
    assert num_decodings("226") == 3
    assert num_decodings("06") == 0
    assert num_decodings("0") == 0
    assert num_decodings("1") == 1
    assert num_decodings("10") == 1
    assert num_decodings("27") == 1
    assert num_decodings("100") == 0
    assert num_decodings("2101") == 1
    assert num_decodings("111111") == 13
    assert num_decodings("1" * 100) == 573147844013817084101
    print("ok")
