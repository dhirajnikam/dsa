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


# O(n) time, O(n) space
# Consume preorder left to right; the inorder index of each root splits the remaining
# inorder range into left and right subtrees.
def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    idx = {v: i for i, v in enumerate(inorder)}
    pre_i = 0

    def helper(lo: int, hi: int) -> TreeNode | None:   # inorder range [lo, hi)
        nonlocal pre_i
        if lo >= hi:
            return None
        val = preorder[pre_i]
        pre_i += 1
        node = TreeNode(val)
        mid = idx[val]
        node.left = helper(lo, mid)
        node.right = helper(mid + 1, hi)
        return node

    return helper(0, len(inorder))
