# O(n * n!) time, O(n) space (excluding output)
# At each depth choose any unused element; mark used, recurse, unmark.
def permute(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    used = [False] * len(nums)

    def dfs(path: list[int]) -> None:
        if len(path) == len(nums):
            res.append(path.copy())
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(x)
            dfs(path)
            path.pop()
            used[i] = False

    dfs([])
    return res
