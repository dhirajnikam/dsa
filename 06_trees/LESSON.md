# 06 · Trees

*New to this topic? Read `THEORY.md` in this folder first. It explains the idea from zero.*

> A tree is the first data structure that is defined in terms of itself: a node, a left tree,
> a right tree. So the algorithms are defined in terms of themselves too. Trust the recursive
> call to be correct on the smaller tree, and most tree problems become three lines.

**Interview frequency:** very high. Amazon asks trees in almost every loop, usually a BST or
a level-order variant. Google uses them to test whether you can reason about recursion
without tracing every call.

## 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** The file system on your laptop is a tree: folders inside
folders, files at the leaves. Every web page is parsed into a tree, the DOM, and the browser
draws it by walking that tree. Org charts are trees. Decision trees in machine-learning models
ask one question per node. Amazon's product catalog is a tree of categories, and "Electronics >
Headphones > Wireless" is a path from the root. `max_depth` here is the same code that measures
how deep a folder hierarchy goes.

**The analogy.** You are a manager asked "how many people report to you, all the way down?" You
do not walk the building. You ask your two direct reports the same question, add their numbers,
add one for yourself, and report back. Each of them does the same. Someone with no reports
answers zero. Nobody in that chain sees the whole company, and the answer is still correct.
That is recursion on a tree: delegate to two smaller trees, trust what comes back, combine.

**How it works, in plain words.** A binary tree is either empty or a node with a left tree and
a right tree. So every tree function has two parts: say what the answer is for the empty tree,
then assume the answers for both subtrees are already in hand and combine them with the node's
value. Depth is one plus the deeper side, with the empty tree at zero; the anchor shows it in
three lines. When a problem needs the tree row by row instead, you switch to a queue and
process one level at a time, the other half of this chapter.

**What learning this will feel like.** Recursion on trees feels like it cannot possibly work.
You will want to trace every call, and on a tree of seven nodes the trace has fifteen calls and
you will lose your place around the ninth. That urge is normal. It is your brain refusing to
trust a function that is not finished yet. The fix is a habit, not a talent: write the empty
case, write the one-node case, check them by hand, then stop tracing. The aha usually lands on
`same_tree` or `diameter`, when the recursive call becomes a promise you can rely on. The trap
to remember: `is_valid_bst` by comparing a node with its children. It passes small examples and
fails when a grandchild is out of range. Pass bounds down instead.

**You will know you have it when** you write a tree function in three lines, run it once, and
feel no need to trace it.

## 1. The core idea

Every binary tree is either empty (`None`) or a root with two smaller binary trees hanging
off it. That single sentence is the whole chapter. To compute anything about a tree:

1. Decide what the answer is for the empty tree. That is your base case.
2. Assume you already know the answer for `root.left` and `root.right`. Do not think about
   how. Combine them with `root.val` into the answer for `root`.

```
trace every call (exhausting)          trust the call (three lines)
depth(A)                               def depth(node):
  depth(B)                                 if not node: return 0
    depth(D) -> 1                          return 1 + max(depth(node.left),
    depth(E) -> 1                                         depth(node.right))
  -> 2
  depth(C) -> 1
-> 3
```

The recognition cue: **any question about a tree that can be answered from the answers for
its two subtrees.** Height, size, sum, "is it a mirror," "is it balanced," "the best path
through here." When the answer needs the *whole* tree at once, which is rare, you use a
level-order (BFS) traversal instead.

The two traversal orders you must own:

- **DFS** (depth-first): follow one branch to the bottom before backing up. Recursion or an
  explicit stack. Preorder (root, left, right), inorder (left, root, right, which visits a
  BST in sorted order), postorder (left, right, root).
- **BFS** (breadth-first): visit all of depth 0, then all of depth 1, and so on. A queue,
  always. Anything with "level," "row," or "nearest" is BFS.

## 2. Anchor problem: Maximum Depth, fully worked

**Problem.** Return the number of nodes on the longest path from the root down to a leaf.
The empty tree has depth 0.

**Understand.** Depth counts nodes, not edges, so a single node has depth 1. Empty tree → 0.
Skewed trees (every node has one child) are allowed, so recursion depth can reach n.

**Examples.** `[3, 9, 20, None, None, 15, 7] → 3` (3 → 20 → 15). `[1, None, 2] → 2`.
`[] → 0`. `[1] → 1`.

**Brute force.** There is no meaningful brute force; every algorithm must visit every node,
so O(n) is the floor. The question is only whether you can write it cleanly.

**Insight.** The depth of a tree is 1 (for the root) plus the depth of the deeper subtree.
The depth of the empty tree is 0. That is a complete definition, and Python will execute a
definition.

**Code, recursive.**

```python
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Code, iterative BFS.** Count how many times you drain the queue.

```python
def max_depth(root):
    if root is None:
        return 0
    queue, depth = deque([root]), 0
    while queue:
        for _ in range(len(queue)):        # exactly the nodes on the current level
            node = queue.popleft()
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        depth += 1
    return depth
```

**Test.** `[3, 9, 20, None, None, 15, 7]`, recursive: depth(3) = 1 + max(depth(9), depth(20)).
depth(9) = 1 + max(0, 0) = 1. depth(20) = 1 + max(depth(15), depth(7)) = 1 + max(1, 1) = 2.
So depth(3) = 1 + max(1, 2) = 3. ✓
BFS: level 0 = [3], depth 1. level 1 = [9, 20], depth 2. level 2 = [15, 7], depth 3. Queue
empty → 3. ✓

**Complexity.** O(n) time. Space O(h) for recursion where h is the height (O(n) worst case for
a skewed tree, O(log n) for a balanced one). BFS space is O(w), the widest level, which can
be n/2.

**What to say out loud.** "Depth is one plus the deeper of the two subtrees, with the empty
tree at zero. That is a direct recursive definition, O(n) time and O(height) stack. If you
are worried about stack depth on a skewed tree of a million nodes, I can do it as a BFS and
count levels."

## 3. Patterns and templates in this chapter

### Recursive DFS skeleton

```python
def solve(node):
    if node is None:
        return BASE                        # answer for the empty tree
    left = solve(node.left)                # trust these
    right = solve(node.right)
    return combine(node.val, left, right)
```

Depth: `BASE = 0`, combine is `1 + max`. Sum: `BASE = 0`, combine is `val + left + right`.
Mirror: recurse on both trees at once, `same(a.left, b.right) and same(a.right, b.left)`.
Every problem in exercises 1 to 6 is this skeleton with a different base and combine.

### BFS level by level with a `len(queue)` snapshot

```python
from collections import deque

def level_order(root):
    out = []
    if root is None:
        return out
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):        # snapshot: only this level's nodes
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        out.append(level)
    return out
```

The `len(queue)` snapshot is the entire trick. Everything in the queue when the `for` starts
is one level; everything you push during it is the next. Right-side view: keep `level[-1]`.
Zigzag: reverse every other level. Minimum depth: return as soon as you pop a leaf.

### BST invariant with (lo, hi) bounds

A binary search tree is not "left child smaller than me, right child larger." It is "every
node in my left subtree is smaller than me, every node in my right subtree is larger." Pass
the allowed range down.

```python
def is_valid_bst(root):
    def ok(node, lo, hi):                  # every val must satisfy lo < val < hi
        if node is None:
            return True
        if not (lo < node.val < hi):
            return False
        return ok(node.left, lo, node.val) and ok(node.right, node.val, hi)
    return ok(root, float("-inf"), float("inf"))
```

Two other BST facts that turn hard problems into easy ones: an inorder traversal visits values
in sorted order (kth smallest is "stop the inorder walk after k nodes"), and the lowest common
ancestor of `p` and `q` is the first node whose value is between them (walk down from the root
in O(h) with no recursion).

### Return value vs. global best

Some problems ask for the best path *anywhere* in the tree, but the recursion naturally
computes something else: the best path *starting here and going down*. Return the second;
update a nonlocal record with the first as a side effect.

```python
def diameter(root):
    best = 0
    def height(node):                      # returns height; updates best on the way
        nonlocal best
        if node is None:
            return 0
        left, right = height(node.left), height(node.right)
        best = max(best, left + right)     # path through node = left height + right height
        return 1 + max(left, right)        # what the parent needs from us
    height(root)
    return best
```

Diameter, maximum path sum, and `is_balanced` (return height, or -1 as a poison value for
"already unbalanced") are all this pattern. The interview signal is that you can name the
two different quantities.

### Rebuilding a tree from traversals

Preorder's first element is the root. Find it in inorder: everything left of it is the left
subtree, everything right is the right subtree. Recurse. A dict from value to inorder index
makes the lookup O(1) and the whole build O(n).

### Serialization

Preorder with a marker for `None` (`"1,2,#,#,3,#,#"`) is unambiguous and trivial to parse
with an iterator: read a token, if it is the marker return `None`, otherwise build the node and
recurse for left, then right. Level-order with markers also works and is what the tests use.

## 4. Recognition cues

| You see | Think |
|---------|-------|
| "depth", "height", "count", "sum", "mirror", "identical" | recursive DFS, base + combine |
| "level", "row", "level order", "right side view", "nearest" | BFS with `len(queue)` snapshot |
| "BST", "sorted", "kth smallest", "validate" | inorder traversal, or (lo, hi) bounds |
| "lowest common ancestor" in a BST | walk down: go left if both smaller, right if both larger |
| "lowest common ancestor" in a plain tree | postorder: return the node found, or the child that found one |
| "diameter", "longest path", "max path sum" | return height-like value, record the best through-path |
| "balanced" | return height, use -1 as "already failed" |
| "build tree from preorder + inorder" | preorder[0] is root, split inorder around it |
| "serialize", "encode a tree" | preorder with `#` for None, or level order with markers |
| "path from root", "good nodes" | pass state (max so far) down as a parameter |

## 5. Pitfalls

- **Checking children instead of subtrees** in `is_valid_bst`. `[5, 1, 4, None, None, 3, 6]`
  passes the child check and is not a BST. Pass bounds.
- **Using `0` as the base for `max_path_sum`.** Values can be negative. The base for "best
  downward path from a child" is 0 only because you may *decline* to take a child; the global
  best must start at negative infinity.
- **Forgetting the `len(queue)` snapshot** turns level-order into a flat list. Iterating
  `for node in queue` while appending is also a bug.
- **Recursion depth.** Python's default limit is 1000. A skewed tree of 10⁴ nodes will crash the
  recursive version. Mention it and offer the iterative one, or `sys.setrecursionlimit`.
- **`is_balanced` with a naive height call** is O(n²). Compute height and balance in one
  postorder pass.
- **Diameter in edges vs. nodes.** LeetCode counts edges: `left + right` where each is a
  height in nodes. Confirm which one the interviewer wants.
- **`is_subtree` by comparing serializations** needs delimiters and a `None` marker, or `"12"`
  matches `"1,2"`. The clean answer is `same_tree` at every node.
- **Mutating the input** in `invert_tree` is expected. In `is_subtree` it is a bug.

## 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|---------|-----------|----------|----------|
| 1 | `max_depth` | Easy | Everyone | The anchor above. `1 + max(left, right)`. |
| 2 | `invert_tree` | Easy | Google, Amazon | Swap the children, then recurse. Return the root. |
| 3 | `same_tree` | Easy | Amazon | Both None → True. One None → False. Vals equal and both subtrees the same. |
| 4 | `is_subtree` | Easy | Amazon | `same_tree(root, sub)` or is_subtree of either child. O(m·n); fine. |
| 5 | `diameter` | Easy | Amazon, Google | Return height; record `left + right` at every node. |
| 6 | `is_balanced` | Easy | Amazon, Google | Return height, or -1 if any subtree is already unbalanced. |
| 7 | `level_order` | Medium | Amazon, Google | BFS with a `len(queue)` snapshot. |
| 8 | `right_side_view` | Medium | Amazon | Level order; keep the last value of each level. |
| 9 | `count_good_nodes` | Medium | Amazon | Pass the maximum on the path so far as a parameter. |
| 10 | `is_valid_bst` | Medium | Amazon, Google | `(lo, hi)` bounds. Do not compare with children. |
| 11 | `kth_smallest_bst` | Medium | Amazon, Google | Inorder walk, count down k. Stop early. |
| 12 | `lowest_common_ancestor_bst` | Medium | Amazon, Google | Walk from the root; stop at the first node between p and q. |
| 13 | `lowest_common_ancestor` | Medium | Amazon, Google | Postorder. If I am p or q, return me. Else return whichever child found something, or me if both did. |
| 14 | `build_from_preorder_inorder` | Medium | Amazon, Google | Preorder's next value is the root. Inorder index tells you the split. |
| 15 | `max_path_sum` | Hard | Google, Amazon | Return the best downward gain from here (never negative). Record `val + left + right`. |
| 16 | `Codec` | Hard | Google, Amazon | Preorder with `#` for None. Deserialize with an iterator over the tokens. |

Solve 1–11 in order. 12–16 are the stretch set; 12 and 13 together, then 14, 15, 16.
