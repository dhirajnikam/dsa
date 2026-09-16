# Trees: combine answers from smaller trees

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Nodes/references and recursion; queues for level-order traversal.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **tree** is a hierarchy without cycles. A binary-tree node has up to two children; a subtree is the tree rooted at one node. A binary search tree adds an ordering rule, but an arbitrary binary tree is not sorted.

Depth-first traversal explores descendants before completing sibling work. Preorder visits a node before children; inorder between them; postorder after them. Breadth-first traversal uses a queue to visit one distance from the root at a time.

Recursive tree thinking asks: “What information should each child return so its parent can finish?” Height, balance, and path problems may need different summaries. Define whether a length counts nodes or edges. Auxiliary memory depends on height for recursion, and maximum frontier width for BFS.

Validating a BST requires respecting ancestor bounds, not just comparing a node with its immediate parent. Lowest common ancestor is about node ancestry, not numerical closeness. Reconstructing a tree from traversals relies on value uniqueness or an explicit way to distinguish duplicates. A maximum path may pass through a node without being extendable through both children to its parent.

## Walk through a small example

A root has a left child with one child of its own and a right leaf. Counting nodes, the leaf subtrees have height 1, the left subtree height 2, and the root height 3. Postorder makes the child facts available before the parent needs them.

## Watch for

Assuming every binary tree is a BST; checking only parent-child ordering; mixing edge count and node count; forgetting empty-tree behavior.

## Your next small step

Open [max depth](problems/01_max_depth.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 11/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Maximum Depth of Binary Tree](problems/01_max_depth.py)
- [Invert Binary Tree](problems/02_invert_tree.py)
- [Same Tree](problems/03_same_tree.py)
- [Binary Tree Level Order Traversal](problems/04_level_order.py)
- [Diameter of Binary Tree](problems/05_diameter.py)
- [Balanced Binary Tree](problems/06_balanced_tree.py)
- [Validate Binary Search Tree](problems/07_validate_bst.py)
- [Kth Smallest Element in a BST](problems/08_kth_smallest_bst.py)
- [Lowest Common Ancestor of a Binary Search Tree](problems/09_lowest_common_ancestor_bst.py)
- [Lowest Common Ancestor of a Binary Tree](problems/10_lowest_common_ancestor_binary_tree.py)
- [Construct Binary Tree from Preorder and Inorder Traversal](problems/11_build_from_preorder_inorder.py)
- [Binary Tree Maximum Path Sum](problems/12_max_path_sum.py)

</details>
