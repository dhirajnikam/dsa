def min_distance(word1, word2):
    # O(n*m) time, O(m) space
    # dp[i][j] = dp[i-1][j-1] if chars match else 1 + min(delete dp[i-1][j],
    # insert dp[i][j-1], replace dp[i-1][j-1]); dp[i][0] = i, dp[0][j] = j.
    m = len(word2)
    prev = list(range(m + 1))
    for i, a in enumerate(word1, 1):
        cur = [i] + [0] * m
        for j, b in enumerate(word2, 1):
            cur[j] = prev[j - 1] if a == b else 1 + min(prev[j], cur[j - 1], prev[j - 1])
        prev = cur
    return prev[m]
