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


# O(h) time, O(1) space
# Walk down: both smaller -> go left, both larger -> go right, else this node splits them.
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    lo, hi = min(p.val, q.val), max(p.val, q.val)
    node = root
    while node:
        if hi < node.val:
            node = node.left
        elif lo > node.val:
            node = node.right
        else:
            return node
    raise ValueError("p and q must be in the tree")


def _find(root: TreeNode | None, val: int) -> TreeNode:
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    assert root is not None
    return root
