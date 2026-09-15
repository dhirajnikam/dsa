def min_path_sum(grid):
    # O(m*n) time, O(n) space
    # dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1]); one rolling row.
    n = len(grid[0])
    row = [float("inf")] * n
    row[0] = 0
    for r in range(len(grid)):
        row[0] += grid[r][0]
        for c in range(1, n):
            row[c] = grid[r][c] + min(row[c], row[c - 1])
    return row[-1]
