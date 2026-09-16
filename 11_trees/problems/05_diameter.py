"""
Problem: Diameter of Binary Tree
Difficulty: Easy | Pattern: Return height, record best (bottom-up)
Source: LeetCode 543

Given the root of a binary tree, return the length of the diameter: the number of edges on
the longest path between any two nodes. The path may or may not pass through the root.

Example 1:
  Input: root = [1,2,3,4,5]
  Output: 3   (path 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)

Example 2:
  Input: root = [1,2]
  Output: 1

Constraints:
  1 <= number of nodes <= 10^4
  -100 <= Node.val <= 100

Hints:
1. The longest path through a node = height(left) + height(right) in edges.
2. Write height(node) that returns 0 for None, and while computing it update a nonlocal best.
3. Return the height, not the diameter. They are different quantities.

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


def diameter_of_binary_tree(root: TreeNode | None) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert diameter_of_binary_tree(build([1, 2, 3, 4, 5])) == 3, 'Check: diameter_of_binary_tree(build([1, 2, 3, 4, 5])) == 3'
    assert diameter_of_binary_tree(build([1, 2])) == 1, 'Check: diameter_of_binary_tree(build([1, 2])) == 1'
    assert diameter_of_binary_tree(build([1])) == 0, 'Check: diameter_of_binary_tree(build([1])) == 0'
    assert diameter_of_binary_tree(None) == 0, 'Check: diameter_of_binary_tree(None) == 0'
    assert diameter_of_binary_tree(build([1, 2, None, 3, None, 4])) == 3, 'Check: diameter_of_binary_tree(build([1, 2, None, 3, None, 4])) == 3'     # skewed: diameter = height
    # longest path 5-3-2-4-6 (4 edges) does not pass through the root
    assert diameter_of_binary_tree(build([1, 2, None, 3, 4, 5, None, None, None, 6])) == 4, 'Check: diameter_of_binary_tree(build([1, 2, None, 3, 4, 5, None, None, None, 6])) == 4'
    assert diameter_of_binary_tree(build([1, 2, 3, 4, 5, 6, 7])) == 4, 'Check: diameter_of_binary_tree(build([1, 2, 3, 4, 5, 6, 7])) == 4'
    print("ok")
