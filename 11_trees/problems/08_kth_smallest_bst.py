"""
Problem: Kth Smallest Element in a BST
Difficulty: Medium | Pattern: Iterative inorder with early stop
Source: LeetCode 230

Given the root of a binary search tree and an integer k, return the k-th smallest value
(1-indexed) of all node values in the tree.

Example 1:
  Input: root = [3,1,4,null,2], k = 1
  Output: 1

Example 2:
  Input: root = [5,3,6,2,4,null,null,1], k = 3
  Output: 3

Constraints:
  1 <= k <= number of nodes <= 10^4
  0 <= Node.val <= 10^4

Hints:
1. Inorder traversal of a BST visits values in ascending order.
2. Iterative inorder with an explicit stack lets you stop after k pops instead of visiting all n nodes.
3. Follow-up: if the tree is modified often, store subtree sizes in each node.

Expected: O(h + k) time, O(h) space.
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


def kth_smallest(root: TreeNode, k: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert kth_smallest(build([3, 1, 4, None, 2]), 1) == 1
    assert kth_smallest(build([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
    assert kth_smallest(build([1]), 1) == 1
    assert kth_smallest(build([2, 1]), 2) == 2
    assert kth_smallest(build([1, None, 2, None, 3, None, 4]), 4) == 4     # right-skewed
    assert kth_smallest(build([4, 3, None, 2, None, 1]), 1) == 1            # left-skewed
    t = build([5, 3, 6, 2, 4, None, None, 1])
    assert [kth_smallest(t, k) for k in range(1, 7)] == [1, 2, 3, 4, 5, 6]
    print("ok")
