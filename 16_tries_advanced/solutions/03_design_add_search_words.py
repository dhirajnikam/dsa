class WordDictionary:
    # add O(L); search O(L) without wildcards, O(26^dots * L) worst case with them
    # Standard dict trie. A '.' fans out over every child; a letter follows one child.
    # Success requires consuming all characters and landing on an end marker.
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return "$" in node
            c = word[i]
            if c == ".":
                return any(dfs(child, i + 1) for k, child in node.items() if k != "$")
            return c in node and dfs(node[c], i + 1)
        return dfs(self.root, 0)
