def find_words(board, words):
    # O(m*n*4*3^(L-1)) worst case time, O(sum of word lengths) space
    # A trie lets every DFS step ask "does any remaining word continue with this letter?"
    # and stop immediately otherwise. Found words are removed from the trie to avoid
    # duplicates and to prune dead branches.
    root = {}
    for w in words:
        node = root
        for c in w:
            node = node.setdefault(c, {})
        node["$"] = w

    m, n = len(board), len(board[0]) if board else 0
    found = []

    def dfs(r, c, parent):
        ch = board[r][c]
        node = parent[ch]
        word = node.pop("$", None)
        if word is not None:
            found.append(word)
        board[r][c] = "#"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in node:
                dfs(nr, nc, node)
        board[r][c] = ch
        if not node:
            parent.pop(ch)

    for r in range(m):
        for c in range(n):
            if board[r][c] in root:
                dfs(r, c, root)
    return found
