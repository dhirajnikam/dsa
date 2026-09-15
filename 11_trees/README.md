# Phase 11: Trees

**Goal:** see a tree problem and know which shape it is: return info up, pass info down, or go level by level.

## Key idea
Almost every tree problem is recursion: solve left child, solve right child, combine here.
Bottom-up calls *return* a value (height). Top-down calls *receive* one (allowed range). "By level" is BFS with a queue. A BST keeps left < node < right, so its inorder walk is sorted.

## Cheat sheet
```python
def diameter(root):                  # bottom-up: return one thing, record another
    best = 0
    def height(node):
        nonlocal best
        if not node: return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)      # the answer, uses both children
        return 1 + max(l, r)         # what the parent needs
    height(root); return best
def valid(node, lo, hi):             # top-down: pass bounds as arguments
    if not node: return True
    return lo < node.val < hi and valid(node.left, lo, node.val) and valid(node.right, node.val, hi)
```

## When you see... use...
- "depth / height / diameter / balanced / max path" -> bottom-up, return a number
- "valid BST / path sum / depends on ancestors" -> top-down, pass parameters
- "level order / right side view / min depth" -> BFS, `for _ in range(len(q))` = one level
- "k-th smallest in BST" -> inorder walk, stop at k
- "lowest common ancestor" -> BST: walk down by value. General tree: postorder

## Common mistakes
- Returning what you should record (height vs diameter). They are different values.
- Checking a BST by comparing only direct children. Pass `lo, hi` bounds.
- Base case is `if not node`, not `if node.left`. The root can be `None`.
- Max path sum with negatives: start `best = -inf`, clamp child gains with `max(0, gain)`.

## Problems
- `01_max_depth.py` — simplest bottom-up
- `02_invert_tree.py` — swap children, recurse
- `03_same_tree.py` — recurse on two trees at once
- `04_level_order.py` — BFS with level snapshot
- `05_diameter.py` — return height, record diameter
- `06_balanced_tree.py` — height, `-1` means unbalanced
- `07_validate_bst.py` — top-down bounds
- `08_kth_smallest_bst.py` — inorder, stop early
- `09_lowest_common_ancestor_bst.py` — walk down by value
- `10_lowest_common_ancestor_binary_tree.py` — postorder LCA
- `11_build_from_preorder_inorder.py` — preorder gives root, inorder splits sides
- `12_max_path_sum.py` — bottom-up with clamping, hard
