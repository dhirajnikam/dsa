def longest_common_subsequence(text1, text2):
    # O(n*m) time, O(min(n, m)) space
    # dp[i][j] = dp[i-1][j-1] + 1 if chars match else max(dp[i-1][j], dp[i][j-1]).
    # Only the previous row is read, so two rows suffice.
    if len(text2) > len(text1):
        text1, text2 = text2, text1
    prev = [0] * (len(text2) + 1)
    for a in text1:
        cur = [0] * (len(text2) + 1)
        for j, b in enumerate(text2, 1):
            cur[j] = prev[j - 1] + 1 if a == b else max(prev[j], cur[j - 1])
        prev = cur
    return prev[-1]
