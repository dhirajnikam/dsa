# O(4^n / sqrt(n)) time (number of valid strings), O(n) space for recursion
# Only add ')' when it would not exceed the '(' count, so every leaf is valid.
def generate_parenthesis(n: int) -> list[str]:
    res: list[str] = []

    def dfs(path: list[str], open_: int, close: int) -> None:
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        if open_ < n:
            path.append("(")
            dfs(path, open_ + 1, close)
            path.pop()
        if close < open_:
            path.append(")")
            dfs(path, open_, close + 1)
            path.pop()

    dfs([], 0, 0)
    return res
