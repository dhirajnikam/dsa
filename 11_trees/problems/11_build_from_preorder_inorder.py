"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium | Pattern: Divide and conquer with index map
Source: LeetCode 105

Given two integer arrays preorder and inorder, the preorder and inorder traversals of the
same binary tree with unique values, construct and return the tree.

Example 1:
  Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
  Output: [3,9,20,null,null,15,7]

Example 2:
  Input: preorder = [-1], inorder = [-1]
  Output: [-1]

Constraints:
  1 <= len(preorder) == len(inorder) <= 3000
  -3000 <= values <= 3000, all unique
  Both arrays are valid traversals of the same tree.

Hints:
1. preorder[0] is the root. Its index in inorder tells you how many nodes are in the left subtree.
2. Slicing both arrays at every level works but is O(n^2). Pass index ranges instead.
3. Build a dict value -> inorder index once, and consume preorder with a moving pointer.

Expected: O(n) time, O(n) space.
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


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    raise NotImplementedError


if __name__ == "__main__":
    assert to_level(build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])) == [3, 9, 20, None, None, 15, 7]
    assert to_level(build_tree([-1], [-1])) == [-1]
    assert build_tree([], []) is None
    assert to_level(build_tree([1, 2], [2, 1])) == [1, 2]
    assert to_level(build_tree([1, 2], [1, 2])) == [1, None, 2]
    assert to_level(build_tree([1, 2, 3, 4], [4, 3, 2, 1])) == [1, 2, None, 3, None, 4]      # left-skewed
    assert to_level(build_tree([1, 2, 3, 4], [1, 2, 3, 4])) == [1, None, 2, None, 3, None, 4]  # right-skewed
    assert to_level(build_tree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])) == [1, 2, 3, 4, 5, 6, 7]
    print("ok")
