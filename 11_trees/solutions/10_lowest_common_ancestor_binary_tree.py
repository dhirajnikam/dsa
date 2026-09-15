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
# Post-order: a node whose left and right searches both find something is the LCA;
# otherwise pass up whichever side found p, q, or the LCA.
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def dfs(node: TreeNode | None) -> TreeNode | None:
        if node is None or node is p or node is q:
            return node
        left, right = dfs(node.left), dfs(node.right)
        if left and right:
            return node
        return left or right

    return dfs(root)


def _find(root: TreeNode | None, val: int) -> TreeNode | None:
    if root is None:
        return None
    if root.val == val:
        return root
    return _find(root.left, val) or _find(root.right, val)
