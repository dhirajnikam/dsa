from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def build(values):
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


def rob(root):
    # O(n) time, O(h) space
    # Post-order returns (rob_this, skip_this): rob = val + children's skip,
    # skip = sum of children's best. Answer is max at the root.
    def dfs(node):
        if not node:
            return 0, 0
        l, r = dfs(node.left), dfs(node.right)
        return node.val + l[1] + r[1], max(l) + max(r)

    return max(dfs(root))
