# O(n * 2^n) time, O(n) space (recursion depth, excluding output)
# Record the path at every node, then extend with each later element.
def subsets(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []

    def dfs(start: int, path: list[int]) -> None:
        res.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])
    return res


def _norm(res: list[list[int]]) -> list[list[int]]:
    return sorted(sorted(s) for s in res)
