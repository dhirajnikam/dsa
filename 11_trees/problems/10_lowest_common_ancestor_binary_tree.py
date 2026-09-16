"""
Problem: Lowest Common Ancestor of a Binary Tree
Difficulty: Medium | Pattern: Post-order LCA
Source: LeetCode 236

Given a binary tree (not a BST) and two nodes p and q in it, return their lowest common
ancestor.

Example 1:
  Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
  Output: 3

Example 2:
  Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
  Output: 5

Example 3:
  Input: root = [1,2], p = 1, q = 2
  Output: 1

Constraints:
  2 <= number of nodes <= 10^5
  All values are unique; p and q exist in the tree and p != q.

Hints:
1. lca(node): if node is None or node is p or node is q, return node.
2. Recurse on both children. If both return non-None, node is the answer.
3. Otherwise return whichever child result is non-None (it is either the LCA found deeper or one of p/q).

Expected: O(n) time, O(h) space.
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


def _find(root: TreeNode | None, val: int) -> TreeNode | None:
    if root is None:
        return None
    if root.val == val:
        return root
    return _find(root.left, val) or _find(root.right, val)


if __name__ == "__main__":
    t = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    lca = lambda a, b: lowest_common_ancestor(t, _find(t, a), _find(t, b)).val
    assert lca(5, 1) == 3, 'Check: lca(5, 1) == 3'
    assert lca(5, 4) == 5, 'Check: lca(5, 4) == 5'
    assert lca(6, 4) == 5, 'Check: lca(6, 4) == 5'
    assert lca(7, 4) == 2, 'Check: lca(7, 4) == 2'
    assert lca(0, 8) == 1, 'Check: lca(0, 8) == 1'
    assert lca(6, 8) == 3, 'Check: lca(6, 8) == 3'
    t2 = build([1, 2])
    assert lowest_common_ancestor(t2, _find(t2, 1), _find(t2, 2)).val == 1, 'Check: lowest_common_ancestor(t2, _find(t2, 1), _find(t2, 2)).val == 1'
    t3 = build([1, None, 2, None, 3, None, 4])
    assert lowest_common_ancestor(t3, _find(t3, 4), _find(t3, 2)).val == 2, 'Check: lowest_common_ancestor(t3, _find(t3, 4), _find(t3, 2)).val == 2'
    print("ok")
