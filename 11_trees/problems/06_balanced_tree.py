"""
Problem: Balanced Binary Tree
Difficulty: Easy | Pattern: Bottom-up with sentinel
Source: LeetCode 110

Given a binary tree, determine if it is height-balanced: for every node, the heights of the
left and right subtrees differ by at most one.

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Output: True

Example 2:
  Input: root = [1,2,2,3,3,null,null,4,4]
  Output: False

Example 3:
  Input: root = []
  Output: True

Constraints:
  0 <= number of nodes <= 5000
  -10^4 <= Node.val <= 10^4

Hints:
1. Naive: at each node compute both heights and recurse. That is O(n log n) to O(n^2).
2. One pass: write height(node) that returns -1 as soon as any subtree is unbalanced.
3. If either child returns -1, or |l - r| > 1, return -1; else return 1 + max(l, r).

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


def is_balanced(root: TreeNode | None) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert is_balanced(build([3, 9, 20, None, None, 15, 7])) is True
    assert is_balanced(build([1, 2, 2, 3, 3, None, None, 4, 4])) is False
    assert is_balanced(None) is True
    assert is_balanced(build([1])) is True
    assert is_balanced(build([1, 2])) is True
    assert is_balanced(build([1, 2, None, 3])) is False                 # skewed depth 3
    assert is_balanced(build([1, 2, 3, 4, None, None, None, 5])) is False
    assert is_balanced(build([1, 2, 3, 4, 5, 6, 7])) is True
    print("ok")
