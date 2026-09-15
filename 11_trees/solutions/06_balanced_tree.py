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


# O(n) time, O(h) space
# Height function that short-circuits with -1 when any subtree is unbalanced.
def is_balanced(root: TreeNode | None) -> bool:
    def height(node: TreeNode | None) -> int:
        if node is None:
            return 0
        l = height(node.left)
        if l < 0:
            return -1
        r = height(node.right)
        if r < 0 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)

    return height(root) >= 0
