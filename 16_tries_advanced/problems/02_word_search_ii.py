"""
Problem: Word Search II
Difficulty: Hard | Pattern: Trie + backtracking DFS
Source: LeetCode 212

Given an m x n board of letters and a list of words, return all words that can be formed
by a path of adjacent cells (up/down/left/right). A cell may be used at most once per word.
Return the words in any order, without duplicates.

Example 1:
  board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
  words = ["oath","pea","eat","rain"] -> ["eat","oath"]
Example 2: board = [["a","b"],["c","d"]], words = ["abcb"] -> []

Hints:
1. Build a trie of the words. DFS from every cell, moving `node = node[ch]` as you go;
   stop the moment the trie has no child for the letter (this is the whole point).
2. Store the full word at its end node; when you reach it, add to results and clear the
   marker so it is not reported twice.
3. Mark the cell visited by writing "#" into the board and restore it after the recursion.
4. Follow-up pruning: delete leaf trie nodes after a word is found so later DFS dies faster.

Expected: O(m*n*4*3^(L-1)) worst-case time, O(total chars in words) space
"""


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    raise NotImplementedError


if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    assert sorted(find_words(board, ["oath", "pea", "eat", "rain"])) == ["eat", "oath"]
    assert find_words([["a", "b"], ["c", "d"]], ["abcb"]) == []
    assert sorted(find_words([["a"]], ["a", "aa"])) == ["a"]
    assert sorted(find_words([["a", "a"]], ["aa", "aaa"])) == ["aa"]
    assert sorted(find_words([["a", "b"], ["c", "d"]], ["ab", "cd", "ac", "bd", "abd", "abcd"])) == ["ab", "abd", "ac", "bd", "cd"]
    assert find_words([["x"]], []) == []
    assert sorted(find_words([["o", "a"], ["h", "t"]], ["oath", "oath"])) == ["oath"]
    print("ok")
