"""
Problem: Lowest Common Ancestor of a Binary Search Tree
Difficulty: Medium | Pattern: BST-guided walk
Source: LeetCode 235

Given a BST and two nodes p and q in it, return their lowest common ancestor: the deepest
node that has both p and q as descendants (a node is a descendant of itself).

Example 1:
  Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
  Output: 6

Example 2:
  Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
  Output: 2

Example 3:
  Input: root = [2,1], p = 2, q = 1
  Output: 2

Constraints:
  2 <= number of nodes <= 10^5
  All values are unique; p and q exist in the tree and p != q.

Hints:
1. If both values are less than the current node, the LCA is in the left subtree.
2. If both are greater, it is in the right subtree.
3. Otherwise the current node splits them (or equals one of them) and is the LCA. No recursion needed.

Expected: O(h) time, O(1) space.
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def build(values: list) -> TreeNode | None:
    """Build a tree from a LeetCode-style level-order list where None marks a missing child."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    raise NotImplementedError


def _find(root: TreeNode | None, val: int) -> TreeNode:
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    assert root is not None
    return root


if __name__ == "__main__":
    t = build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    lca = lambda a, b: lowest_common_ancestor(t, _find(t, a), _find(t, b)).val
    assert lca(2, 8) == 6
    assert lca(2, 4) == 2
    assert lca(3, 5) == 4
    assert lca(0, 5) == 2
    assert lca(7, 9) == 8
    assert lca(0, 9) == 6
    t2 = build([2, 1])
    assert lowest_common_ancestor(t2, _find(t2, 2), _find(t2, 1)).val == 2
    t3 = build([1, None, 2, None, 3])
    assert lowest_common_ancestor(t3, _find(t3, 2), _find(t3, 3)).val == 2
    print("ok")
