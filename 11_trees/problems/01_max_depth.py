"""
Problem: Maximum Depth of Binary Tree
Difficulty: Easy | Pattern: Bottom-up DFS
Source: LeetCode 104

Given the root of a binary tree, return its maximum depth: the number of nodes along the
longest path from the root down to the farthest leaf.

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Output: 3

Example 2:
  Input: root = [1,null,2]
  Output: 2

Constraints:
  0 <= number of nodes <= 10^4
  -100 <= Node.val <= 100

Hints:
1. Depth of an empty tree is 0.
2. Depth of a node = 1 + max(depth(left), depth(right)).
3. Try an iterative BFS version too: count levels.

Expected: O(n) time, O(h) space where h is the height.
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


def max_depth(root: TreeNode | None) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert max_depth(build([3, 9, 20, None, None, 15, 7])) == 3, 'Check: max_depth(build([3, 9, 20, None, None, 15, 7])) == 3'
    assert max_depth(build([1, None, 2])) == 2, 'Check: max_depth(build([1, None, 2])) == 2'
    assert max_depth(None) == 0, 'Check: max_depth(None) == 0'
    assert max_depth(build([1])) == 1, 'Check: max_depth(build([1])) == 1'
    assert max_depth(build([1, 2, None, 3, None, 4])) == 4, 'Check: max_depth(build([1, 2, None, 3, None, 4])) == 4'       # left-skewed
    assert max_depth(build([1, None, 2, None, 3, None, 4])) == 4, 'Check: max_depth(build([1, None, 2, None, 3, None, 4])) == 4'  # right-skewed
    assert max_depth(build([1, 2, 3, 4, 5, 6, 7])) == 3, 'Check: max_depth(build([1, 2, 3, 4, 5, 6, 7])) == 3'            # perfect
    # Boundary and misconception checks: predict each result before running.
    assert max_depth(build([0, 0, 0])) == 2, 'Check: max_depth(build([0, 0, 0])) == 2'
    print("ok")
