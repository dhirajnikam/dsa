# 06 · Trees

**In one sentence.** A tree is a box with two smaller trees hanging off it, so anything you want
to know about the whole tree can be built from what you know about the two smaller ones.

**Why you care.** Your file system is a tree. Every web page is parsed into a tree before the
browser draws it. Interview frequency is very high. Amazon asks trees in almost every loop.
Google uses them to test whether you can trust recursion without tracing every call.

## The idea, with a story

Open the Documents folder on your laptop. Inside are folders. Inside those, more folders.
Eventually you hit files, which contain nothing. That is a tree. The top folder is the root.
Each folder is a node. The files at the bottom are leaves.

Now the delegation story. You are the CEO and want to know how many levels deep the company
goes. You do not walk the building. You ask your two VPs: "how many levels are below you,
counting yourself?" Each VP asks their managers the same question. At the bottom, someone with
no reports answers "1, just me." Answers flow back up. Each person takes the bigger of the two
answers they got and adds 1 for themself.

You never saw the whole company. You trusted the same question asked of a smaller piece. That
is tree recursion. Reading the org chart one row at a time, CEO, then all VPs, then all
managers, is the other move. That is breadth-first.

## The same story with numbers

A tree with five nodes. Each node has a value, a left child, and a right child.

```
        3
       / \
      9   20
         /  \
        15   7
```

How deep is it? Ask each node "how deep is the tree below you, counting yourself?" An empty
spot answers 0.

| Node | Left answer | Right answer | 1 + bigger of the two |
|------|-------------|--------------|-----------------------|
| 15 | 0 | 0 | 1 |
| 7 | 0 | 0 | 1 |
| 9 | 0 | 0 | 1 |
| 20 | 1 | 1 | 2 |
| 3 | 1 | 2 | 3 |

Depth 3. The same function ran at every node.

Pause and predict: what does the breadth-first reading of this tree look like, one row per line?

<details><summary>Answer</summary>
Row 0: 3. Row 1: 9, 20. Row 2: 15, 7. Three rows, another way to get depth 3.
</details>

## The anchor problem: Maximum Depth

Return the number of nodes on the longest path from the root down to a leaf. Empty tree is 0.

**Brute force.** None worth naming. Every answer must visit every node, so O(n) is the floor.

**Insight.** Depth is 1 for the root plus the depth of the deeper subtree. The empty tree has
depth 0. That is a complete definition, and Python will run a definition.

```python
def max_depth(root):
    if root is None:                   # base case: the empty tree
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Complexity.** O(n) time, O(h) stack space where h is the height. A chain makes h equal n.

**What to say.** "Depth is one plus the deeper subtree, with the empty tree at zero. O(n) time,
O(height) stack. If a skewed tree worries you, I can count levels with a queue instead."

## Templates you memorize

**Recursive DFS skeleton.** Exercises 1 to 6 are this with a different base and combine.
```python
def solve(node):
    if node is None:
        return BASE                    # answer for the empty tree
    left = solve(node.left)            # trust these
    right = solve(node.right)
    return combine(node.val, left, right)
```
Depth: base 0, combine `1 + max`. Sum: base 0, combine `val + left + right`. Mirror: recurse on
two trees at once, `same(a.left, b.right) and same(a.right, b.left)`.

**BFS level by level.** The `len(queue)` snapshot is the entire trick. Everything in the queue
when the `for` starts is one level. Everything you push during it is the next.
```python
from collections import deque

def level_order(root):
    out, queue = [], deque([root] if root else [])
    while queue:
        level = []
        for _ in range(len(queue)):    # only this level's nodes
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        out.append(level)
    return out
```
Right side view: keep `level[-1]`. Minimum depth: return when you pop a leaf.

**BST bounds check.** A binary search tree is not "left child smaller, right child larger." It is
"everything in the left subtree smaller, everything in the right subtree larger." Pass the
allowed range down.
```python
def is_valid_bst(root):
    def ok(node, lo, hi):              # every val must satisfy lo < val < hi
        if node is None:
            return True
        if not (lo < node.val < hi):
            return False
        return ok(node.left, lo, node.val) and ok(node.right, node.val, hi)
    return ok(root, float("-inf"), float("inf"))
```
Two more BST facts. An inorder walk visits values in sorted order. The lowest common ancestor
of two values is the first node whose value sits between them.

**Return one thing, record another.** Some problems want the best path anywhere. The recursion
naturally computes the best path going down from here. Return the second, record the first.
```python
def diameter(root):
    best = 0
    def height(node):
        nonlocal best
        if node is None:
            return 0
        left, right = height(node.left), height(node.right)
        best = max(best, left + right)  # path through this node
        return 1 + max(left, right)     # what the parent needs
    height(root)
    return best
```

## When you see X, think Y

| You see | Think |
|---------|-------|
| "depth", "count", "sum", "mirror", "identical" | recursive DFS, base plus combine |
| "level", "row", "right side view" | BFS with the `len(queue)` snapshot |
| "BST", "validate", "kth smallest" | `(lo, hi)` bounds, or an inorder walk |
| "lowest common ancestor" in a BST | walk down: left if both smaller, right if both larger |
| "lowest common ancestor" in a plain tree | return the node found, or the child that found one |
| "diameter", "longest path", "max path sum" | return height, record the best through-path |
| "balanced" | return height, use -1 as "already failed" |
| "serialize" | preorder with `#` for None |

## Words you will hear

- **Node, root, leaf.** One box. The top box. A box with no children.
- **Subtree.** A node with everything below it. Every node is the root of its own subtree.
- **Base case.** The answer for the empty tree. Always your first line.
- **DFS, depth-first.** Go all the way down one branch before backing up. Recursion does this.
- **BFS, breadth-first.** Visit row 0, then row 1, and so on. Needs a queue. Output is level order.
- **Inorder.** Left, node, right. On a BST it comes out sorted.
- **BST, binary search tree.** Smaller on the left, bigger on the right, at every node.

## Mistakes everyone makes once

- **Checking children instead of subtrees** in `is_valid_bst`. Tree `[5, 1, 4, None, None, 3, 6]`
  passes the child check and is not a BST. Pass bounds down.
- **Forgetting the `len(queue)` snapshot.** Level order collapses into one flat list.
- **Starting the global best at 0** in `max_path_sum`. Values can be negative. Start at negative
  infinity.
- **Tracing every call.** Check the empty case and the one-node case by hand. Check the combine
  line assuming the children are right. Then stop tracing.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO. The file already has `TreeNode`,
`build_tree`, and `to_level_list` as helpers. Read them once. They are not exercises.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `max_depth` | Easy | The anchor. `1 + max(left, right)`. |
| 2 | `invert_tree` | Easy | Swap the children, then recurse. Return the root. |
| 3 | `same_tree` | Easy | Both None: True. One None: False. Values equal and both subtrees same. |
| 4 | `is_subtree` | Easy | `same_tree(root, sub)` or is_subtree of either child. |
| 5 | `diameter` | Easy | Return height. Record `left + right` at every node. |
| 6 | `is_balanced` | Easy | Return height, or -1 if a subtree is already unbalanced. |
| 7 | `level_order` | Medium | BFS with a `len(queue)` snapshot. |
| 8 | `right_side_view` | Medium | Level order. Keep the last value of each level. |
| 9 | `count_good_nodes` | Medium | Pass the maximum on the path so far as a parameter. |
| 10 | `is_valid_bst` | Medium | `(lo, hi)` bounds. Do not compare with children. |
| 11 | `kth_smallest_bst` | Medium | Inorder walk. Count down k. Stop early. |
| 12 | `lowest_common_ancestor_bst` | Medium | Walk from the root. Stop at the first node between p and q. |
| 13 | `lowest_common_ancestor` | Medium | If I am p or q, return me. Else return the child that found one, or me if both did. |
| 14 | `build_from_preorder_inorder` | Medium | Preorder's next value is the root. Its inorder index gives the split. |
| 15 | `max_path_sum` | Hard | Return the best downward gain, never negative. Record `val + left + right`. |
| 16 | `Codec` | Hard | Preorder with `#` for None. Deserialize with an iterator over the tokens. |

Do 1 and 3 today with a 30-minute timer. Then 7, so you have written one DFS and one BFS before
touching a BST. 2 to 11 over the week. 12 to 16 are for when the first eleven pass cold.
