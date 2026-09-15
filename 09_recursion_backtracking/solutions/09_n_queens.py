# O(n!) time, O(n) space (excluding output)
# One queen per row; sets of used columns and both diagonals (r-c, r+c) make the attack check O(1).
def solve_n_queens(n: int) -> list[list[str]]:
    res: list[list[str]] = []
    cols: set[int] = set()
    diag: set[int] = set()
    anti: set[int] = set()
    placement: list[int] = []

    def dfs(r: int) -> None:
        if r == n:
            res.append(["." * c + "Q" + "." * (n - c - 1) for c in placement])
            return
        for c in range(n):
            if c in cols or (r - c) in diag or (r + c) in anti:
                continue
            cols.add(c); diag.add(r - c); anti.add(r + c); placement.append(c)
            dfs(r + 1)
            cols.remove(c); diag.remove(r - c); anti.remove(r + c); placement.pop()

    dfs(0)
    return res


def _no_attacks(board: list[str]) -> bool:
    cols = [row.index("Q") for row in board]
    n = len(board)
    if any(row.count("Q") != 1 or len(row) != n for row in board):
        return False
    for i in range(n):
        for j in range(i + 1, n):
            if cols[i] == cols[j] or abs(cols[i] - cols[j]) == j - i:
                return False
    return True
