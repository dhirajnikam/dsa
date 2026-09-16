"""06 · Trees — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.

TreeNode, build_tree and to_level_list below are helpers, not exercises. Read them once.
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def build_tree(values: list) -> Optional[TreeNode]:
    """Build a tree from a LeetCode-style level-order list. None marks a missing child.
    [3, 9, 20, None, None, 15, 7] ->      3
                                        /   \\
                                       9     20
                                            /  \\
                                           15   7
    """
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def to_level_list(root: Optional[TreeNode]) -> list:
    """Inverse of build_tree: level-order list with None for missing children,
    trailing Nones removed. to_level_list(build_tree(x)) == x for canonical x.
    """
    out: list = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


# ----------------------------------------------------------------------------- problems

def max_depth(root: Optional[TreeNode]) -> int:
    """Number of nodes on the longest root-to-leaf path. Empty tree -> 0.
    [3, 9, 20, None, None, 15, 7] -> 3 ; [1, None, 2] -> 2 ; [] -> 0
    """
    raise NotImplementedError


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Mirror the tree in place (swap left and right at every node) and return the root.
    [4, 2, 7, 1, 3, 6, 9] -> [4, 7, 2, 9, 6, 3, 1] ; [2, 1, 3] -> [2, 3, 1] ; [] -> []
    """
    raise NotImplementedError


def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """True if both trees have the same shape and the same values at every position.
    [1, 2, 3], [1, 2, 3] -> True ; [1, 2], [1, None, 2] -> False ; [], [] -> True
    """
    raise NotImplementedError


def is_subtree(root: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
    """True if some node of root, together with all of its descendants, is identical to sub.
    [3, 4, 5, 1, 2], [4, 1, 2] -> True ; [3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2] -> False
    """
    raise NotImplementedError


def diameter(root: Optional[TreeNode]) -> int:
    """Length in EDGES of the longest path between any two nodes. The path need not pass
    through the root.
    [1, 2, 3, 4, 5] -> 3  (4-2-1-3 or 5-2-1-3) ; [1, 2] -> 1 ; [1] -> 0
    """
    raise NotImplementedError


def is_balanced(root: Optional[TreeNode]) -> bool:
    """True if at every node the heights of the two subtrees differ by at most 1. O(n).
    [3, 9, 20, None, None, 15, 7] -> True ; [1, 2, 2, 3, 3, None, None, 4, 4] -> False ; [] -> True
    """
    raise NotImplementedError


def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    """Values grouped by depth, top to bottom, left to right within a level.
    [3, 9, 20, None, None, 15, 7] -> [[3], [9, 20], [15, 7]] ; [1] -> [[1]] ; [] -> []
    """
    raise NotImplementedError


def right_side_view(root: Optional[TreeNode]) -> list[int]:
    """The rightmost value on each level, top to bottom.
    [1, 2, 3, None, 5, None, 4] -> [1, 3, 4] ; [1, None, 3] -> [1, 3] ; [1, 2] -> [1, 2]
    """
    raise NotImplementedError


def count_good_nodes(root: Optional[TreeNode]) -> int:
    """A node is good if no value on the path from the root to it is greater than its own
    value. The root is always good. Count the good nodes.
    [3, 1, 4, 3, None, 1, 5] -> 4 ; [3, 3, None, 4, 2] -> 3 ; [1] -> 1
    """
    raise NotImplementedError


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """True if every node's value is strictly greater than everything in its left subtree
    and strictly less than everything in its right subtree.
    [2, 1, 3] -> True ; [5, 1, 4, None, None, 3, 6] -> False ; [5, 4, 6, None, None, 3, 7] -> False
    """
    raise NotImplementedError


def kth_smallest_bst(root: Optional[TreeNode], k: int) -> int:
    """The kth smallest value (1-indexed) in a BST with distinct values.
    [3, 1, 4, None, 2], 1 -> 1 ; [5, 3, 6, 2, 4, None, None, 1], 3 -> 3
    """
    raise NotImplementedError


def lowest_common_ancestor_bst(root: Optional[TreeNode], p_val: int, q_val: int) -> int:
    """Value of the deepest node in a BST that has both p_val and q_val as descendants
    (a node counts as its own descendant). Both values exist in the tree. O(h).
    [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8 -> 6 ; same, 2, 4 -> 2 ; [2, 1], 2, 1 -> 2
    """
    raise NotImplementedError


def lowest_common_ancestor(root: Optional[TreeNode], p_val: int, q_val: int) -> int:
    """Same as above for any binary tree with distinct values (no ordering to exploit).
    [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1 -> 3 ; same, 5, 4 -> 5 ; [1, 2], 1, 2 -> 1
    """
    raise NotImplementedError


def build_from_preorder_inorder(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    """Rebuild the unique tree (distinct values) with these preorder and inorder traversals.
    [3, 9, 20, 15, 7], [9, 3, 15, 20, 7] -> [3, 9, 20, None, None, 15, 7] ; [-1], [-1] -> [-1]
    """
    raise NotImplementedError


def max_path_sum(root: Optional[TreeNode]) -> int:
    """Largest sum of values along any path (a sequence of adjacent nodes, each used once,
    at least one node). The path need not go through the root or touch a leaf.
    [1, 2, 3] -> 6 ; [-10, 9, 20, None, None, 15, 7] -> 42 ; [-3] -> -3
    """
    raise NotImplementedError


class Codec:
    """serialize(root) -> str and deserialize(s) -> root such that the round trip rebuilds
    the identical tree. Any format you like; the test compares via to_level_list.
    Hint: preorder with a marker for None, then parse with an iterator.
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        raise NotImplementedError

    def deserialize(self, data: str) -> Optional[TreeNode]:
        raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_max_depth():
    assert max_depth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth(build_tree([1, None, 2])) == 2
    assert max_depth(build_tree([])) == 0
    assert max_depth(build_tree([1])) == 1
    assert max_depth(build_tree([1, 2, None, 3, None, 4])) == 4


def _t_02_invert_tree():
    assert to_level_list(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert to_level_list(invert_tree(build_tree([2, 1, 3]))) == [2, 3, 1]
    assert to_level_list(invert_tree(build_tree([]))) == []
    assert to_level_list(invert_tree(build_tree([1, 2]))) == [1, None, 2]


def _t_03_same_tree():
    assert same_tree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True
    assert same_tree(build_tree([1, 2]), build_tree([1, None, 2])) is False
    assert same_tree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) is False
    assert same_tree(build_tree([]), build_tree([])) is True
    assert same_tree(build_tree([1]), build_tree([])) is False


def _t_04_is_subtree():
    assert is_subtree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2])) is True
    assert is_subtree(build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]),
                      build_tree([4, 1, 2])) is False
    assert is_subtree(build_tree([1]), build_tree([1])) is True
    assert is_subtree(build_tree([1, 2]), build_tree([2])) is True
    assert is_subtree(build_tree([1, 2]), build_tree([1])) is False


def _t_05_diameter():
    assert diameter(build_tree([1, 2, 3, 4, 5])) == 3
    assert diameter(build_tree([1, 2])) == 1
    assert diameter(build_tree([1])) == 0
    assert diameter(build_tree([])) == 0
    # longest path avoids the root: 4-3-2-5-6 has 4 edges
    assert diameter(build_tree([1, 2, None, 3, 5, 4, None, None, None, None, 6])) == 4


def _t_06_is_balanced():
    assert is_balanced(build_tree([3, 9, 20, None, None, 15, 7])) is True
    assert is_balanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])) is False
    assert is_balanced(build_tree([])) is True
    assert is_balanced(build_tree([1, 2, None, 3])) is False
    assert is_balanced(build_tree([1, 2, 3, 4, None, None, None])) is True


def _t_07_level_order():
    assert level_order(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert level_order(build_tree([1])) == [[1]]
    assert level_order(build_tree([])) == []
    assert level_order(build_tree([1, 2, None, 3])) == [[1], [2], [3]]


def _t_08_right_side_view():
    assert right_side_view(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert right_side_view(build_tree([1, None, 3])) == [1, 3]
    assert right_side_view(build_tree([1, 2])) == [1, 2]
    assert right_side_view(build_tree([])) == []
    # level 2 only exists on the left side
    assert right_side_view(build_tree([1, 2, 3, 4])) == [1, 3, 4]


def _t_09_count_good_nodes():
    assert count_good_nodes(build_tree([3, 1, 4, 3, None, 1, 5])) == 4
    assert count_good_nodes(build_tree([3, 3, None, 4, 2])) == 3
    assert count_good_nodes(build_tree([1])) == 1
    assert count_good_nodes(build_tree([9, 8, 7, 6, 5, 4, 3])) == 1
    assert count_good_nodes(build_tree([-1, 5, -2, 4, 4, 2, -4])) == 3   # -1, 5, 2


def _t_10_is_valid_bst():
    assert is_valid_bst(build_tree([2, 1, 3])) is True
    assert is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])) is False
    assert is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7])) is False   # 3 is under 5's right
    assert is_valid_bst(build_tree([])) is True
    assert is_valid_bst(build_tree([2, 2])) is False                          # equal not allowed
    assert is_valid_bst(build_tree([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])) is True


def _t_11_kth_smallest_bst():
    assert kth_smallest_bst(build_tree([3, 1, 4, None, 2]), 1) == 1
    assert kth_smallest_bst(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
    assert kth_smallest_bst(build_tree([5, 3, 6, 2, 4, None, None, 1]), 6) == 6
    assert kth_smallest_bst(build_tree([1]), 1) == 1
    assert kth_smallest_bst(build_tree([2, 1, 3]), 2) == 2


def _t_12_lowest_common_ancestor_bst():
    t = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert lowest_common_ancestor_bst(t, 2, 8) == 6
    assert lowest_common_ancestor_bst(t, 2, 4) == 2
    assert lowest_common_ancestor_bst(t, 3, 5) == 4
    assert lowest_common_ancestor_bst(t, 0, 5) == 2
    assert lowest_common_ancestor_bst(build_tree([2, 1]), 2, 1) == 2


def _t_13_lowest_common_ancestor():
    t = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert lowest_common_ancestor(t, 5, 1) == 3
    assert lowest_common_ancestor(t, 5, 4) == 5
    assert lowest_common_ancestor(t, 7, 4) == 2
    assert lowest_common_ancestor(t, 6, 8) == 3
    assert lowest_common_ancestor(build_tree([1, 2]), 1, 2) == 1


def _t_14_build_from_preorder_inorder():
    got = build_from_preorder_inorder([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert to_level_list(got) == [3, 9, 20, None, None, 15, 7]
    assert to_level_list(build_from_preorder_inorder([-1], [-1])) == [-1]
    assert to_level_list(build_from_preorder_inorder([], [])) == []
    assert to_level_list(build_from_preorder_inorder([1, 2, 3], [3, 2, 1])) == [1, 2, None, 3]
    assert to_level_list(build_from_preorder_inorder([1, 2, 3], [1, 2, 3])) == [1, None, 2, None, 3]


def _t_15_max_path_sum():
    assert max_path_sum(build_tree([1, 2, 3])) == 6
    assert max_path_sum(build_tree([-10, 9, 20, None, None, 15, 7])) == 42
    assert max_path_sum(build_tree([-3])) == -3
    assert max_path_sum(build_tree([-2, -1])) == -1
    assert max_path_sum(build_tree([2, -1, -2])) == 2
    assert max_path_sum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 48


def _t_16_codec():
    codec = Codec()
    for case in ([], [1], [1, 2, 3, None, None, 4, 5], [1, None, 2, None, 3],
                 [-5, 0, 10, None, 7], [1, 2, None, 3, None, 4]):
        s = codec.serialize(build_tree(case))
        assert isinstance(s, str), type(s)
        assert to_level_list(codec.deserialize(s)) == case, case


def _check():
    checks = [(n[3:], f) for n, f in sorted(globals().items()) if n.startswith("_t_")]
    passed = 0
    for name, fn in checks:
        try:
            fn()
            print(f"PASS  {name}")
            passed += 1
        except NotImplementedError:
            print(f"TODO  {name}")
        except AssertionError as e:
            print(f"FAIL  {name}  {e}")
        except Exception as e:  # noqa: BLE001 — show the student what blew up
            print(f"FAIL  {name}  {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(checks)} passed")


if __name__ == "__main__":
    _check()
