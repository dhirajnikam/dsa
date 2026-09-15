"""
Problem: Validate Binary Search Tree
Difficulty: Medium | Pattern: Top-down DFS with bounds
Source: LeetCode 98

Given the root of a binary tree, determine if it is a valid BST: for every node, all values
in its left subtree are strictly less than the node's value and all values in its right
subtree are strictly greater. Both subtrees must also be BSTs.

Example 1:
  Input: root = [2,1,3]
  Output: True

Example 2:
  Input: root = [5,1,4,null,null,3,6]
  Output: False  (4 is in the right subtree of 5 but 3 < 5)

Constraints:
  1 <= number of nodes <= 10^4
  -2^31 <= Node.val <= 2^31 - 1

Hints:
1. Checking only node.left.val < node.val < node.right.val is not enough (see example 2).
2. Pass an open interval (lo, hi) down: valid(node, lo, hi) requires lo < node.val < hi.
3. Use None or +-infinity for unbounded sides. Alternative: inorder traversal must be strictly increasing.

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


def is_valid_bst(root: TreeNode | None) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert is_valid_bst(build([2, 1, 3])) is True
    assert is_valid_bst(build([5, 1, 4, None, None, 3, 6])) is False
    assert is_valid_bst(build([1])) is True
    assert is_valid_bst(None) is True
    assert is_valid_bst(build([5, 4, 6, None, None, 3, 7])) is False   # deep violation
    assert is_valid_bst(build([2, 2, 2])) is False                       # duplicates not allowed
    assert is_valid_bst(build([1, None, 2, None, 3])) is True            # right-skewed increasing
    assert is_valid_bst(build([3, 2, None, 1])) is True                  # left-skewed decreasing
    assert is_valid_bst(build([2147483647])) is True
    assert is_valid_bst(build([-2147483648, None, 2147483647])) is True
    print("ok")
