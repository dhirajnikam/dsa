"""
Problem: Binary Tree Level Order Traversal
Difficulty: Medium | Pattern: BFS with level snapshot
Source: LeetCode 102

Given the root of a binary tree, return the level order traversal of its nodes' values
(left to right, level by level).

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Output: [[3],[9,20],[15,7]]

Example 2:
  Input: root = [1]
  Output: [[1]]

Example 3:
  Input: root = []
  Output: []

Constraints:
  0 <= number of nodes <= 2000
  -1000 <= Node.val <= 1000

Hints:
1. Use a deque. Start with the root (if any).
2. For each level, record len(q) first, then pop exactly that many nodes.
3. Children appended during a level are processed in the next outer iteration.

Expected: O(n) time, O(w) space where w is the max width.
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


def level_order(root: TreeNode | None) -> list[list[int]]:
    raise NotImplementedError


if __name__ == "__main__":
    assert level_order(build([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert level_order(build([1])) == [[1]]
    assert level_order(None) == []
    assert level_order(build([1, 2, None, 3])) == [[1], [2], [3]]
    assert level_order(build([1, None, 2, None, 3])) == [[1], [2], [3]]
    assert level_order(build([1, 2, 3, 4, 5, 6, 7])) == [[1], [2, 3], [4, 5, 6, 7]]
    assert level_order(build([1, 2, 3, None, 4, None, 5])) == [[1], [2, 3], [4, 5]]
    print("ok")
