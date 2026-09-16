"""
Problem: Same Tree
Difficulty: Easy | Pattern: Parallel DFS on two trees
Source: LeetCode 100

Given the roots of two binary trees p and q, return True if they are structurally identical
and the nodes have the same values.

Example 1:
  Input: p = [1,2,3], q = [1,2,3]
  Output: True

Example 2:
  Input: p = [1,2], q = [1,null,2]
  Output: False

Example 3:
  Input: p = [1,2,1], q = [1,1,2]
  Output: False

Constraints:
  0 <= number of nodes in each tree <= 100
  -10^4 <= Node.val <= 10^4

Hints:
1. Both None: same. Exactly one None: different.
2. Otherwise compare values and recurse on (p.left, q.left) and (p.right, q.right).
3. Iteratively, push pairs onto a stack.

Expected: O(min(n, m)) time, O(h) space.
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


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    raise NotImplementedError


if __name__ == "__main__":
    assert is_same_tree(build([1, 2, 3]), build([1, 2, 3])) is True, 'Check: is_same_tree(build([1, 2, 3]), build([1, 2, 3])) is True'
    assert is_same_tree(build([1, 2]), build([1, None, 2])) is False, 'Check: is_same_tree(build([1, 2]), build([1, None, 2])) is False'
    assert is_same_tree(build([1, 2, 1]), build([1, 1, 2])) is False, 'Check: is_same_tree(build([1, 2, 1]), build([1, 1, 2])) is False'
    assert is_same_tree(None, None) is True, 'Check: is_same_tree(None, None) is True'
    assert is_same_tree(build([1]), None) is False, 'Check: is_same_tree(build([1]), None) is False'
    assert is_same_tree(None, build([1])) is False, 'Check: is_same_tree(None, build([1])) is False'
    assert is_same_tree(build([1, 2, 3, 4]), build([1, 2, 3])) is False, 'Check: is_same_tree(build([1, 2, 3, 4]), build([1, 2, 3])) is False'
    assert is_same_tree(build([1, 2, 3, None, 4]), build([1, 2, 3, None, 4])) is True, 'Check: is_same_tree(build([1, 2, 3, None, 4]), build([1, 2, 3, None, 4])) is True'
    print("ok")
