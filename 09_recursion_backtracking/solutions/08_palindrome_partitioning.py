# O(n * 2^n) time, O(n) space for recursion (excluding output)
# At each start index try every end whose substring is a palindrome, then recurse from end.
def partition(s: str) -> list[list[str]]:
    res: list[list[str]] = []

    def dfs(start: int, path: list[str]) -> None:
        if start == len(s):
            res.append(path.copy())
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece == piece[::-1]:
                path.append(piece)
                dfs(end, path)
                path.pop()

    dfs(0, [])
    return res
