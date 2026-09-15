class Trie:
    # O(L) per operation, O(total chars) space
    # Each node is a dict of children plus an end flag; walking a prefix visits one node
    # per character, so cost is independent of how many words are stored.
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def _walk(self, prefix):
        node = self.root
        for c in prefix:
            node = node.get(c)
            if node is None:
                return None
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and "$" in node

    def starts_with(self, prefix):
        return self._walk(prefix) is not None
