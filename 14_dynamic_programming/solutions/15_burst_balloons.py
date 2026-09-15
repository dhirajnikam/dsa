def max_coins(nums):
    # O(n^3) time, O(n^2) space
    # Pad with 1s. dp[i][j] = best coins bursting everything strictly between i and j
    # = max over k in (i, j) of dp[i][k] + dp[k][j] + a[i]*a[k]*a[j], where k bursts LAST.
    a = [1] + nums + [1]
    n = len(a)
    dp = [[0] * n for _ in range(n)]
    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = max(dp[i][k] + dp[k][j] + a[i] * a[k] * a[j] for k in range(i + 1, j))
    return dp[0][n - 1]
