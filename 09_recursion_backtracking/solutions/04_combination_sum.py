# O(n^(target/min)) time worst case, O(target/min) space for recursion depth
# Start-index DFS that recurses with i (reuse allowed); sorted input lets us break when a candidate is too big.
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    candidates = sorted(candidates)
    res: list[list[int]] = []

    def dfs(start: int, remaining: int, path: list[int]) -> None:
        if remaining == 0:
            res.append(path.copy())
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                break
            path.append(c)
            dfs(i, remaining - c, path)
            path.pop()

    dfs(0, target, [])
    return res


def _norm(res):
    return sorted(sorted(c) for c in res)
