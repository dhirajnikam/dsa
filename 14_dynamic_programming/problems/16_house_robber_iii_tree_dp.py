"""
Problem: House Robber III
Difficulty: Medium | Pattern: DP on trees (post-order, two states per node)
Source: LeetCode 337

Houses form a binary tree. The thief cannot rob two directly linked houses (parent and
child). Return the maximum amount that can be robbed.

Example 1:
  root = [3, 2, 3, None, 3, None, 1] -> 7   (3 + 3 + 1)
Example 2:
  root = [3, 4, 5, 1, 3, None, 1] -> 9   (4 + 5)

Constraints:
  1 <= number of nodes <= 10^4
  0 <= Node.val <= 10^4

Hints:
1. State per subtree: (best if we rob this node, best if we skip this node).
2. Recurrence: rob = node.val + left.skip + right.skip; skip = max(left) + max(right).
   Return max(dfs(root)).
3. A naive memo on "rob(node)" that re-explores grandchildren is O(n) too but is slower
   and easy to get wrong; the two-state return is the clean version.

Expected: O(n) time, O(h) space
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def build(values: list) -> Optional[TreeNode]:
    """Build a tree from a level-order list with None for missing nodes (LeetCode style)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    for node in queue:
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


def rob(root: Optional[TreeNode]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert rob(build([3, 2, 3, None, 3, None, 1])) == 7
    assert rob(build([3, 4, 5, 1, 3, None, 1])) == 9
    assert rob(build([5])) == 5
    assert rob(build([])) == 0
    assert rob(build([1, 2])) == 2
    assert rob(build([2, 1, 3, None, 4])) == 7
    assert rob(build([4, 1, None, 2, None, 3])) == 7
    assert rob(build([0, 0, 0])) == 0
    chain = build([1] + [i % 2 for i in range(1, 30)])  # small deep-ish tree
    assert rob(chain) >= 1
    print("ok")
