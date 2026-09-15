"""
Problem: Binary Tree Maximum Path Sum
Difficulty: Hard | Pattern: Bottom-up with negative clamping
Source: LeetCode 124

A path is any sequence of nodes where each adjacent pair is connected by an edge and a node
appears at most once. It does not need to pass through the root. The path sum is the sum of
node values on it. Return the maximum path sum of any non-empty path.

Example 1:
  Input: root = [1,2,3]
  Output: 6   (2 -> 1 -> 3)

Example 2:
  Input: root = [-10,9,20,null,null,15,7]
  Output: 42  (15 -> 20 -> 7)

Constraints:
  1 <= number of nodes <= 3 * 10^4
  -1000 <= Node.val <= 1000

Hints:
1. Same shape as diameter: gain(node) returns the best downward path starting at node.
2. gain(node) = node.val + max(0, gain(left), gain(right)). Clamp negative children at 0.
3. Candidate answer at node = node.val + max(0, left_gain) + max(0, right_gain). Start best at -inf.

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


def max_path_sum(root: TreeNode) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert max_path_sum(build([1, 2, 3])) == 6
    assert max_path_sum(build([-10, 9, 20, None, None, 15, 7])) == 42
    assert max_path_sum(build([-3])) == -3                       # single negative node
    assert max_path_sum(build([-2, -1, -3])) == -1               # all negative: pick the best single node
    assert max_path_sum(build([2, -1, -2])) == 2
    assert max_path_sum(build([1, -2, 3])) == 4
    assert max_path_sum(build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 48
    assert max_path_sum(build([1, 2, None, 3, None, 4])) == 10   # skewed: whole chain
    assert max_path_sum(build([-1, -2, 10, -6, None, -3, -6])) == 10
    print("ok")
