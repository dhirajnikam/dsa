"""
Problem: Invert Binary Tree
Difficulty: Easy | Pattern: DFS with in-place mutation
Source: LeetCode 226

Given the root of a binary tree, invert the tree (mirror it) and return its root.

Example 1:
  Input: root = [4,2,7,1,3,6,9]
  Output: [4,7,2,9,6,3,1]

Example 2:
  Input: root = [2,1,3]
  Output: [2,3,1]

Example 3:
  Input: root = []
  Output: []

Constraints:
  0 <= number of nodes <= 100
  -100 <= Node.val <= 100

Hints:
1. Swap root.left and root.right, then recurse into both children.
2. Order does not matter (pre or post order both work).
3. Iterative: a stack or queue of nodes, swap children as you pop.

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



def to_level(root: TreeNode | None) -> list:
    """Inverse of build: level-order list with None for missing children, trailing Nones stripped."""
    out: list = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    raise NotImplementedError


if __name__ == "__main__":
    assert to_level(invert_tree(build([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert to_level(invert_tree(build([2, 1, 3]))) == [2, 3, 1]
    assert invert_tree(None) is None
    assert to_level(invert_tree(build([1]))) == [1]
    assert to_level(invert_tree(build([1, 2]))) == [1, None, 2]
    assert to_level(invert_tree(build([1, None, 2, None, 3]))) == [1, 2, None, 3]
    assert to_level(invert_tree(invert_tree(build([1, 2, 3, 4, None, None, 5])))) == [1, 2, 3, 4, None, None, 5]
    print("ok")
