def num_decodings(s):
    # O(n) time, O(1) space
    # dp[i] = dp[i-1] if s[i-1] is a valid single digit, plus dp[i-2] if s[i-2:i] is 10..26.
    prev2, prev1 = 1, 1 if s[0] != "0" else 0  # dp[0], dp[1]
    for i in range(2, len(s) + 1):
        cur = 0
        if s[i - 1] != "0":
            cur += prev1
        if 10 <= int(s[i - 2:i]) <= 26:
            cur += prev2
        prev2, prev1 = prev1, cur
    return prev1
