def max_area_of_island(grid):
    # O(m*n) time, O(m*n) space
    # DFS returns the size of the island it sinks; take the max over all starting cells.
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != 1:
            return 0
        grid[r][c] = 0
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    return max((dfs(r, c) for r in range(rows) for c in range(cols)), default=0)
