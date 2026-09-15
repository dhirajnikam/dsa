def unique_paths(m, n):
    # O(m*n) time, O(n) space
    # dp[r][c] = dp[r-1][c] + dp[r][c-1]; a single row updated left to right holds both terms.
    row = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            row[c] += row[c - 1]
    return row[-1]
