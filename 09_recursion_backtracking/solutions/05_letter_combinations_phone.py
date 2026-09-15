# O(n * 4^n) time, O(n) space (excluding output)
# Depth-by-digit DFS; each level appends one letter for the current digit.
KEYPAD = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
}


def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []
    res: list[str] = []

    def dfs(i: int, path: list[str]) -> None:
        if i == len(digits):
            res.append("".join(path))
            return
        for ch in KEYPAD[digits[i]]:
            path.append(ch)
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])
    return res
