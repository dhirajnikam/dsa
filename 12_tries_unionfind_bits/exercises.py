"""12 · Tries, Union-Find & Bits — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
"""


# ----------------------------------------------------------------------------- helper types

class TrieNode:
    """One node of a trie. `children` maps a character to the next node; `is_end` marks
    that a stored word finishes here. Fully implemented; use it in Trie, WordDictionary,
    and find_words.
    """

    __slots__ = ("children", "is_end", "word")

    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False
        self.word: str | None = None      # optional: store the full word at its end node

    def __repr__(self) -> str:
        return f"TrieNode(children={sorted(self.children)}, is_end={self.is_end})"


# ----------------------------------------------------------------------------- problems

class Trie:
    """insert(word), search(word) -> exact word present?, starts_with(prefix) -> any word
    begins with prefix? Lowercase letters. Each operation O(len).
    insert("apple"); search("apple") -> True; search("app") -> False; starts_with("app") -> True
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def starts_with(self, prefix: str) -> bool:
        raise NotImplementedError


class WordDictionary:
    """add_word(word); search(pattern) where '.' in the pattern matches any one letter.
    add "bad", "dad", "mad"; search("pad") -> False; search(".ad") -> True; search("b..") -> True
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def add_word(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    """Return every word from `words` that can be traced in the grid by moving to
    horizontally or vertically adjacent cells without reusing a cell. Each word at most once;
    order does not matter (the test sorts). Words are distinct.
    [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        ["oath","pea","eat","rain"] -> ["eat","oath"]
    [["a","b"],["c","d"]], ["abcb"] -> []
    """
    raise NotImplementedError


def longest_common_prefix(strs: list[str]) -> str:
    """Longest string that is a prefix of every string in strs. "" if none or strs is empty.
    ["flower","flow","flight"] -> "fl" ; ["dog","racecar","car"] -> "" ; ["a"] -> "a"
    """
    raise NotImplementedError


class UnionFind:
    """Disjoint sets over items 0..n-1.
    find(x) -> representative of x's group (with path compression).
    union(a, b) -> True if two different groups were merged, False if already together.
    count() -> current number of groups.
    UnionFind(5): count() 5; union(0,1) True; union(1,0) False; count() 4; find(0) == find(1)
    """

    def __init__(self, n: int) -> None:
        raise NotImplementedError

    def find(self, x: int) -> int:
        raise NotImplementedError

    def union(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError


def num_provinces(is_connected: list[list[int]]) -> int:
    """is_connected[i][j] == 1 means cities i and j are directly connected. A province is a
    group of cities connected directly or indirectly. Count the provinces.
    [[1,1,0],[1,1,0],[0,0,1]] -> 2 ; [[1,0,0],[0,1,0],[0,0,1]] -> 3 ; [[1]] -> 1
    """
    raise NotImplementedError


def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    """accounts[i] = [name, email, email, ...]. Two accounts belong to the same person if
    they share any email (names may repeat across different people). Return the merged
    accounts, each as [name, *emails]. The test sorts emails within an account and sorts
    accounts by their first email, so any order is fine.
    [["John","johnsmith@mail.com","john_newyork@mail.com"],
     ["John","johnsmith@mail.com","john00@mail.com"],
     ["Mary","mary@mail.com"],
     ["John","johnnybravo@mail.com"]]
        -> [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
            ["Mary","mary@mail.com"], ["John","johnnybravo@mail.com"]]
    """
    raise NotImplementedError


def num_islands_ii(m: int, n: int, positions: list[list[int]]) -> list[int]:
    """Start with an all-water m x n grid. positions[k] = [r, c] turns that cell to land.
    Return the number of islands (4-directionally connected land) after each operation.
    Adding a cell that is already land changes nothing.
    3, 3, [[0,0],[0,1],[1,2],[2,1]] -> [1, 1, 2, 3] ; 1, 1, [[0,0],[0,0]] -> [1, 1]
    """
    raise NotImplementedError


def single_number(nums: list[int]) -> int:
    """Every value appears exactly twice except one, which appears once. Find it in O(n)
    time and O(1) space.
    [2,2,1] -> 1 ; [4,1,2,1,2] -> 4 ; [1] -> 1
    """
    raise NotImplementedError


def count_bits_in_int(n: int) -> int:
    """Number of 1 bits in the binary representation of a non-negative integer (Hamming weight).
    11 -> 3 ; 128 -> 1 ; 0 -> 0
    """
    raise NotImplementedError


def counting_bits(n: int) -> list[int]:
    """bits[i] = number of 1 bits in i, for i in 0..n. Aim for O(n) using earlier answers.
    2 -> [0,1,1] ; 5 -> [0,1,1,2,1,2] ; 0 -> [0]
    """
    raise NotImplementedError


def reverse_bits(n: int) -> int:
    """Reverse the 32 bits of an unsigned 32-bit integer.
    43261596 (00000010100101000001111010011100) -> 964176192 (00111001011110000010100101000000)
    0 -> 0 ; 1 -> 2147483648
    """
    raise NotImplementedError


def missing_number(nums: list[int]) -> int:
    """nums holds n distinct values from 0..n, so exactly one is missing. Return it.
    [3,0,1] -> 2 ; [0,1] -> 2 ; [0] -> 1
    """
    raise NotImplementedError


def get_sum_no_plus(a: int, b: int) -> int:
    """Return a + b without using + or -. Inputs fit in a signed 32-bit int, and so does the
    result. Handle negatives (two's complement with a 32-bit mask).
    1, 2 -> 3 ; -2, -3 -> -5 ; -1, 1 -> 0
    """
    raise NotImplementedError


def power_of_two(n: int) -> bool:
    """True if n is 2^k for some integer k >= 0.
    1 -> True ; 16 -> True ; 3 -> False ; 0 -> False ; -16 -> False
    """
    raise NotImplementedError


def max_xor_of_two_numbers(nums: list[int]) -> int:
    """Maximum of nums[i] ^ nums[j] over all pairs (i may equal j). Values are non-negative
    and fit in 31 bits. Aim for O(n * 31) with a bitwise trie.
    [3,10,5,25,2,8] -> 28 (5 ^ 25) ; [0] -> 0 ; [2,4] -> 6
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_trie():
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.starts_with("app") is True
    assert t.search("apples") is False
    assert t.starts_with("b") is False
    t.insert("app")
    assert t.search("app") is True
    assert t.starts_with("") is True


def _t_02_word_dictionary():
    wd = WordDictionary()
    assert wd.search("a") is False
    for w in ("bad", "dad", "mad"):
        wd.add_word(w)
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True
    assert wd.search("b...") is False
    assert wd.search("...") is True
    assert wd.search("..") is False


def _t_03_find_words():
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    assert sorted(find_words(board, ["oath", "pea", "eat", "rain"])) == ["eat", "oath"]
    assert board[0][0] == "o", "board must be restored after the search"
    assert find_words([["a", "b"], ["c", "d"]], ["abcb"]) == []
    assert sorted(find_words([["a"]], ["a", "aa"])) == ["a"]
    assert sorted(find_words([["a", "a"]], ["aa", "aaa"])) == ["aa"]
    assert sorted(find_words([["a", "b"], ["c", "d"]], ["ab", "cd", "ac", "bd", "abdc", "ad"])) == \
        ["ab", "abdc", "ac", "bd", "cd"]


def _t_04_longest_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix(["a"]) == "a"
    assert longest_common_prefix(["", "abc"]) == ""
    assert longest_common_prefix([]) == ""
    assert longest_common_prefix(["abc", "abc"]) == "abc"


def _t_05_union_find():
    uf = UnionFind(5)
    assert uf.count() == 5
    assert uf.union(0, 1) is True
    assert uf.union(1, 0) is False
    assert uf.count() == 4
    assert uf.find(0) == uf.find(1)
    assert uf.find(2) != uf.find(0)
    assert uf.union(2, 3) is True
    assert uf.union(1, 3) is True
    assert uf.count() == 2
    assert uf.find(0) == uf.find(3)
    assert uf.find(4) == 4


def _t_06_num_provinces():
    assert num_provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert num_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert num_provinces([[1]]) == 1
    assert num_provinces([[1, 1], [1, 1]]) == 1
    assert num_provinces([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 1


def _t_07_accounts_merge():
    def norm(accs):
        return sorted(([a[0]] + sorted(a[1:]) for a in accs), key=lambda a: a[1])
    got = accounts_merge([["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                          ["John", "johnsmith@mail.com", "john00@mail.com"],
                          ["Mary", "mary@mail.com"],
                          ["John", "johnnybravo@mail.com"]])
    assert norm(got) == [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
                         ["John", "johnnybravo@mail.com"],
                         ["Mary", "mary@mail.com"]], norm(got)
    got = accounts_merge([["A", "a@x", "b@x"], ["A", "c@x", "d@x"], ["A", "b@x", "c@x"]])
    assert norm(got) == [["A", "a@x", "b@x", "c@x", "d@x"]], norm(got)
    got = accounts_merge([["Gabe", "Gabe0@m.co", "Gabe3@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co"]])
    assert norm(got) == [["Gabe", "Gabe0@m.co", "Gabe3@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co"]]
    assert accounts_merge([]) == []


def _t_08_num_islands_ii():
    assert num_islands_ii(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]) == [1, 1, 2, 3]
    assert num_islands_ii(1, 1, [[0, 0], [0, 0]]) == [1, 1]
    assert num_islands_ii(3, 3, [[0, 0], [1, 1], [0, 1]]) == [1, 2, 1]
    assert num_islands_ii(2, 2, []) == []
    assert num_islands_ii(1, 5, [[0, 0], [0, 4], [0, 2], [0, 1], [0, 3]]) == [1, 2, 3, 2, 1]


def _t_09_single_number():
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
    assert single_number([-3, 5, -3]) == 5


def _t_10_count_bits_in_int():
    assert count_bits_in_int(11) == 3
    assert count_bits_in_int(128) == 1
    assert count_bits_in_int(0) == 0
    assert count_bits_in_int(0xFFFFFFFF) == 32


def _t_11_counting_bits():
    assert counting_bits(2) == [0, 1, 1]
    assert counting_bits(5) == [0, 1, 1, 2, 1, 2]
    assert counting_bits(0) == [0]
    assert counting_bits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]


def _t_12_reverse_bits():
    assert reverse_bits(0b00000010100101000001111010011100) == 964176192
    assert reverse_bits(0b11111111111111111111111111111101) == 3221225471
    assert reverse_bits(0) == 0
    assert reverse_bits(1) == 2147483648


def _t_13_missing_number():
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([0, 1]) == 2
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert missing_number([0]) == 1
    assert missing_number([1]) == 0


def _t_14_get_sum_no_plus():
    assert get_sum_no_plus(1, 2) == 3
    assert get_sum_no_plus(2, 3) == 5
    assert get_sum_no_plus(-1, 1) == 0
    assert get_sum_no_plus(-2, -3) == -5
    assert get_sum_no_plus(0, 0) == 0
    assert get_sum_no_plus(1000, -2000) == -1000
    assert get_sum_no_plus(2147483647, -1) == 2147483646


def _t_15_power_of_two():
    assert power_of_two(1) is True
    assert power_of_two(16) is True
    assert power_of_two(3) is False
    assert power_of_two(0) is False
    assert power_of_two(-16) is False
    assert power_of_two(2 ** 40) is True


def _t_16_max_xor_of_two_numbers():
    assert max_xor_of_two_numbers([3, 10, 5, 25, 2, 8]) == 28
    assert max_xor_of_two_numbers([0]) == 0
    assert max_xor_of_two_numbers([2, 4]) == 6
    assert max_xor_of_two_numbers([8, 10, 2]) == 10
    assert max_xor_of_two_numbers([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]) == 127


def _check():
    checks = [(n[3:], f) for n, f in sorted(globals().items()) if n.startswith("_t_")]
    passed = 0
    for name, fn in checks:
        try:
            fn()
            print(f"PASS  {name}")
            passed += 1
        except NotImplementedError:
            print(f"TODO  {name}")
        except AssertionError as e:
            print(f"FAIL  {name}  {e}")
        except Exception as e:  # noqa: BLE001 — show the student what blew up
            print(f"FAIL  {name}  {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(checks)} passed")


if __name__ == "__main__":
    _check()
