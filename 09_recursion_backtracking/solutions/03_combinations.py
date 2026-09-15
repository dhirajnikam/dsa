# O(k * C(n, k)) time, O(k) space (excluding output)
# Start-index DFS; the loop bound prunes branches that cannot reach length k.
def combine(n: int, k: int) -> list[list[int]]:
    res: list[list[int]] = []

    def dfs(start: int, path: list[int]) -> None:
        if len(path) == k:
            res.append(path.copy())
            return
        need = k - len(path)
        for i in range(start, n - need + 2):
            path.append(i)
            dfs(i + 1, path)
            path.pop()

    dfs(1, [])
    return res
