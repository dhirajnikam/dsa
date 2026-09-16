"""12 · Tries, Union-Find & Bits — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""
from collections import defaultdict

from exercises import TrieNode


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())   # create the path as needed
        node.is_end = True

    def _walk(self, s: str) -> TrieNode | None:
        node = self.root
        for c in s:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
    # Every operation O(L) in the length of the word or prefix.


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        def match(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.is_end
            c = word[i]
            if c == ".":
                return any(match(child, i + 1) for child in node.children.values())
            child = node.children.get(c)
            return child is not None and match(child, i + 1)
        return match(self.root, 0)
    # add O(L); search O(L) without dots, up to O(26^dots * L) with them.


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    root = TrieNode()
    for w in words:                                   # one trie for every word
        node = root
        for c in w:
            node = node.children.setdefault(c, TrieNode())
        node.word = w

    rows, cols = len(board), len(board[0])
    found: list[str] = []

    def dfs(r: int, c: int, parent: TrieNode) -> None:
        ch = board[r][c]
        node = parent.children.get(ch)
        if node is None:
            return
        if node.word is not None:
            found.append(node.word)
            node.word = None                          # each word reported once
        board[r][c] = "#"                             # mark visited
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, node)
        board[r][c] = ch                              # unmark
        if not node.children and node.word is None:
            del parent.children[ch]                   # prune: nothing left below this node

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    return found
    # O(cells * 4^L) worst case, but the trie and pruning make it fast in practice.


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    lo, hi = min(strs), max(strs)                     # lexicographic extremes bound everything
    i = 0
    while i < min(len(lo), len(hi)) and lo[i] == hi[i]:
        i += 1
    return lo[:i]
    # O(total characters). Trie version: insert all, walk while exactly one child and not is_end.


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.groups = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra                               # union by rank
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.groups -= 1
        return True

    def count(self) -> int:
        return self.groups
    # Amortized O(alpha(n)) per operation: effectively constant.


def num_provinces(is_connected: list[list[int]]) -> int:
    n = len(is_connected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j]:
                uf.union(i, j)
    return uf.count()
    # O(n^2) to read the matrix.


def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    email_to_id: dict[str, int] = {}                  # email -> index of first account seen
    uf = UnionFind(len(accounts))
    for i, (_, *emails) in enumerate(accounts):
        for e in emails:
            if e in email_to_id:
                uf.union(i, email_to_id[e])           # shared email joins the accounts
            else:
                email_to_id[e] = i
    groups: dict[int, list[str]] = defaultdict(list)
    for e, i in email_to_id.items():
        groups[uf.find(i)].append(e)
    return [[accounts[root][0]] + sorted(emails) for root, emails in groups.items()]
    # O(E log E) for the sorts, where E is the total number of emails.


def num_islands_ii(m: int, n: int, positions: list[list[int]]) -> list[int]:
    uf = UnionFind(m * n)
    land: set[int] = set()
    out: list[int] = []
    count = 0
    for r, c in positions:
        cell = r * n + c
        if cell in land:                              # already land: nothing changes
            out.append(count)
            continue
        land.add(cell)
        count += 1
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < m and 0 <= nc < n and nr * n + nc in land:
                if uf.union(cell, nr * n + nc):
                    count -= 1                        # two islands became one
        out.append(count)
    return out
    # O(k * alpha) for k positions, O(m * n) space.


def single_number(nums: list[int]) -> int:
    x = 0
    for v in nums:
        x ^= v                                        # pairs cancel
    return x


def count_bits_in_int(n: int) -> int:
    count = 0
    while n:
        n &= n - 1                                    # clear the lowest set bit
        count += 1
    return count
    # O(number of set bits).


def counting_bits(n: int) -> list[int]:
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)              # drop the last bit, add it back
    return bits
    # O(n).


def reverse_bits(n: int) -> int:
    out = 0
    for _ in range(32):
        out = (out << 1) | (n & 1)                    # shift the lowest bit of n into out
        n >>= 1
    return out
    # O(32).


def missing_number(nums: list[int]) -> int:
    x = len(nums)                                     # index n has no partner in nums
    for i, v in enumerate(nums):
        x ^= i ^ v
    return x
    # O(n) time, O(1) space. Sum formula n*(n+1)//2 - sum(nums) also works.


def get_sum_no_plus(a: int, b: int) -> int:
    MASK, MAX = 0xFFFFFFFF, 0x7FFFFFFF
    a, b = a & MASK, b & MASK
    while b:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK  # sum without carry, then the carries
    return a if a <= MAX else ~(a ^ MASK)             # reinterpret as signed 32-bit
    # O(32) iterations at most.


def power_of_two(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0


def max_xor_of_two_numbers(nums: list[int]) -> int:
    root: dict = {}                                   # bitwise trie: {0: {...}, 1: {...}}
    for x in nums:
        node = root
        for k in range(30, -1, -1):                   # most significant bit first
            node = node.setdefault((x >> k) & 1, {})
    best = 0
    for x in nums:
        node, cur = root, 0
        for k in range(30, -1, -1):
            bit = (x >> k) & 1
            want = 1 - bit                            # opposite bit makes this XOR bit 1
            if want in node:
                cur |= 1 << k
                node = node[want]
            else:
                node = node[bit]
        best = max(best, cur)
    return best
    # O(n * 31) time and space.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
