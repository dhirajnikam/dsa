def climb_stairs(n):
    # O(n) time, O(1) space
    # dp[i] = dp[i-1] + dp[i-2] (last move was 1 or 2 steps); keep only the last two values.
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
