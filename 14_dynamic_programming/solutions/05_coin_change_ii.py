def change(amount, coins):
    # O(amount * len(coins)) time, O(amount) space
    # dp[a] += dp[a - c] with coins in the outer loop, so each combination is counted once.
    dp = [1] + [0] * amount
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
