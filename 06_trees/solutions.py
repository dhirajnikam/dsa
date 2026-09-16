"""06 · Trees — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""
from collections import deque
from typing import Optional

from exercises import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
    # O(n) time, O(h) stack. BFS version in LESSON.md counts levels with a queue.


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
    # O(n) time, O(h) space.


def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None or q is None:
        return p is q                  # both None -> True; exactly one None -> False
    return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)
    # O(min(m, n)).


def is_subtree(root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
    if root is None:
        return sub is None
    if same_tree(root, sub):
        return True
    return is_subtree(root.left, sub) or is_subtree(root.right, sub)
    # O(m * n) worst case. Serializing both with delimiters and doing substring search is O(m + n).


def diameter(root: Optional[TreeNode]) -> int:
    best = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0
        left, right = height(node.left), height(node.right)
        best = max(best, left + right)         # longest path THROUGH node, in edges
        return 1 + max(left, right)            # what the parent needs: height in nodes

    height(root)
    return best
    # O(n). "Return one thing, record another" pattern.


def is_balanced(root: Optional[TreeNode]) -> bool:
    def height(node: Optional[TreeNode]) -> int:   # height, or -1 if already unbalanced
        if node is None:
            return 0
        left = height(node.left)
        if left < 0:
            return -1
        right = height(node.right)
        if right < 0 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) >= 0
    # O(n) single pass. Calling a separate height() at every node would be O(n^2).


def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    out: list[list[int]] = []
    if root is None:
        return out
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):            # snapshot: exactly this level's nodes
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        out.append(level)
    return out
    # O(n) time, O(w) space for the widest level.


def right_side_view(root: Optional[TreeNode]) -> list[int]:
    return [level[-1] for level in level_order(root)]
    # O(n). A DFS that visits right first and records the first node at each new depth also works.


def count_good_nodes(root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode], path_max: int) -> int:
        if node is None:
            return 0
        good = 1 if node.val >= path_max else 0
        path_max = max(path_max, node.val)
        return good + dfs(node.left, path_max) + dfs(node.right, path_max)

    return dfs(root, float("-inf"))
    # O(n). State flows DOWN as a parameter; counts flow UP as return values.


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def ok(node: Optional[TreeNode], lo: float, hi: float) -> bool:
        if node is None:
            return True
        if not (lo < node.val < hi):
            return False
        return ok(node.left, lo, node.val) and ok(node.right, node.val, hi)

    return ok(root, float("-inf"), float("inf"))
    # O(n). Bounds, not child comparisons.


def kth_smallest_bst(root: Optional[TreeNode], k: int) -> int:
    stack: list[TreeNode] = []
    node = root
    while stack or node:               # iterative inorder; stops after k pops
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    raise ValueError("k larger than tree")
    # O(h + k) time, O(h) space.


def lowest_common_ancestor_bst(root: Optional[TreeNode], p_val: int, q_val: int) -> int:
    lo, hi = min(p_val, q_val), max(p_val, q_val)
    node = root
    while node:
        if hi < node.val:
            node = node.left           # both are smaller: LCA is to the left
        elif lo > node.val:
            node = node.right          # both are larger: LCA is to the right
        else:
            return node.val            # split point (or node equals one of them)
    raise ValueError("values not in tree")
    # O(h) time, O(1) space. No recursion needed because the BST tells you which way to go.


def lowest_common_ancestor(root: Optional[TreeNode], p_val: int, q_val: int) -> int:
    def find(node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node is None or node.val in (p_val, q_val):
            return node                # found one of the targets (or nothing)
        left, right = find(node.left), find(node.right)
        if left and right:
            return node                # one on each side: this is the split point
        return left or right           # pass up whatever was found below

    return find(root).val
    # O(n) time, O(h) space. Postorder: children report before the parent decides.


def build_from_preorder_inorder(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    index = {v: i for i, v in enumerate(inorder)}   # value -> inorder position
    pre_i = 0

    def build(lo: int, hi: int) -> Optional[TreeNode]:   # inorder slice [lo, hi)
        nonlocal pre_i
        if lo >= hi:
            return None
        val = preorder[pre_i]
        pre_i += 1
        node = TreeNode(val)
        mid = index[val]
        node.left = build(lo, mid)     # left subtree consumes the next preorder values
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(inorder))
    # O(n) time and space thanks to the index dict. Slicing lists instead would be O(n^2).


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")               # values can all be negative; do not start at 0

    def gain(node: Optional[TreeNode]) -> int:   # best downward path starting at node, >= 0
        nonlocal best
        if node is None:
            return 0
        left = max(gain(node.left), 0)          # a negative branch is simply not taken
        right = max(gain(node.right), 0)
        best = max(best, node.val + left + right)   # path that bends at node
        return node.val + max(left, right)          # path that continues up to the parent

    gain(root)
    return best
    # O(n). Same shape as diameter: return one quantity, record another.


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        out: list[str] = []

        def pre(node: Optional[TreeNode]) -> None:
            if node is None:
                out.append("#")
                return
            out.append(str(node.val))
            pre(node.left)
            pre(node.right)

        pre(root)
        return ",".join(out)
        # Preorder with "#" for None is unambiguous: every subtree ends exactly where its
        # last "#" does.

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))

        def build() -> Optional[TreeNode]:
            tok = next(tokens)
            if tok == "#":
                return None
            node = TreeNode(int(tok))
            node.left = build()        # the iterator remembers where we are
            node.right = build()
            return node

        return build()
        # O(n) both ways.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
