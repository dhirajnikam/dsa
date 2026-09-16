# 06 · Trees, explained from zero

Read this first if "recursion on a tree" makes you want to trace every call and you lose your
place around the ninth one. When it clicks, open `LESSON.md`, the dense reference. This file is
the patient conversation before it.

## In one sentence

A tree is a box with two smaller trees hanging off it, so anything you want to know about the
whole tree can be built from what you know about the two smaller ones.

## Start with something you already do

Open the Documents folder on your laptop. Inside are folders. Inside those, more folders.
Eventually you hit files, which contain nothing. Nobody finds this confusing. That is a tree.
The top folder is the **root**, each folder is a **node**, and the files at the bottom, with
nothing inside, are **leaves**.

Now the delegation story. You are the CEO and want to know how many levels deep the company
goes. You do not walk the building. You ask your two VPs: "how many levels are below you,
counting yourself?" Each VP asks their managers the same question. At the bottom, someone with
no reports answers "1, just me." Answers flow back up. Each person takes the bigger of the two
answers they got and adds 1 for themself. You never saw the whole company. You trusted the same
question asked of a smaller piece.

That is the sentence that makes tree recursion possible: **a tree is a box with two smaller
trees hanging off it.** The smaller trees are also trees, so whatever question you are
answering, ask it of them and trust the answer.

Two more everyday moves. Reading the org chart one row at a time, CEO, then all VPs, then all
managers, is **breadth-first**. Following one chain of command from the CEO to the bottom, then
backing up and following the next chain, is **depth-first**.

## Now the same thing with numbers

A tree with five nodes. Each node has a value, a left child, and a right child. A missing child
is drawn as nothing.

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
| 20 | 1 (from 15) | 1 (from 7) | 2 |
| 3 | 1 (from 9) | 2 (from 20) | 3 |

Depth 3. The same function ran at every node. In code it is three lines:

```python
def max_depth(node):
    if node is None:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

Pause and predict: what does the breadth-first reading of this tree look like, one row per line?

<details><summary>Answer</summary>
Row 0: 3. Row 1: 9, 20. Row 2: 15, 7. Three rows, another way to get depth 3. A depth-first
reading that visits each node before its children gives 3, 9, 20, 15, 7.
</details>

## The words people use

- **Node.** One box: a value plus links to a left child and a right child. The boxes below a
  node are its children; it is their parent.
- **Root.** The top node. The CEO. The one you are handed.
- **Leaf.** A node with no children. A file, not a folder.
- **Subtree.** A node with everything below it. Every node is the root of its own subtree,
  which is why the same function works everywhere.
- **Binary tree.** Each node has at most two children. Every tree in this chapter is binary.
- **Empty tree / `None`.** A tree with no nodes. Its answer is always your first move.
- **Depth, height.** Nodes on the longest path from the root down to a leaf. A single node has
  depth 1. The lesson writes it `h`.
- **Base case.** The answer for the empty tree, needing no further calls.
- **Combine.** The one line that turns the two children's answers into this node's answer.
- **DFS, depth-first search.** Go all the way down one branch before backing up. Recursion does
  this for free.
- **Preorder, inorder, postorder.** Three depth-first orders: visit the node before, between, or
  after its children. Inorder on a BST comes out sorted.
- **BFS, breadth-first search.** Visit every node at row 0, then row 1, and so on. Needs a
  queue. Its output as a list of rows is called **level order**.
- **Queue.** A line at a shop: first in, first out. Python's `deque` with `popleft()`.
- **BST, binary search tree.** A sorted tree: everything in the left subtree is smaller than
  the node, everything in the right subtree is bigger. A filing cabinet where every drawer says
  "smaller on the left, bigger on the right."
- **Invariant.** A rule that must hold everywhere, like the BST rule. You check it by passing
  allowed bounds `(lo, hi)` down.
- **Lowest common ancestor, LCA.** The deepest node with both given nodes below it. The
  lowest-ranking manager both employees report up to.
- **Diameter.** The longest path between any two nodes, counted in edges.
- **Balanced.** No node's two subtrees differ in height by more than 1.
- **Serialize.** Turn a tree into a string you can save and rebuild from.

## Why the fast way is fast

Every tree algorithm here touches each node once, so time is O(n) no matter what: 10 nodes, 10
visits; 100,000 nodes, 100,000 visits. There is no slow way to beat. The differences are in
memory and in what the shape lets you do.

Recursion uses the call stack, one frame per level you are inside. For a balanced tree that is
about log n frames: 4 for 10 nodes, 10 for 1,000, 17 for 100,000. For a long chain where every
node has one child, it is n frames, and Python gives up around 1,000. BFS instead holds one
whole row in the queue, which can be half the tree.

The real speed win is the BST. In a plain list, finding a value means checking everything. In a
balanced BST you go left or right at each node, so 100,000 values take about 17 steps. That is
chapter 5's binary search in a tree costume.

The trade-off: recursion can run out of stack on tall trees, and a BST is only fast while it
stays balanced. Feed it sorted input and it becomes a chain.

## Try it in your head

1. Root 5, left child 1, right child 4, and 4 has children 3 and 6. Does it obey the BST rule?

<details><summary>Answer</summary>
No. 4 is in the right subtree of 5, so everything under 4 must also be bigger than 5. The 3
breaks that. Checking only "is my child on the correct side of me" would wrongly say yes,
which is the pitfall the lesson warns about. Pass bounds down instead.
</details>

2. You want the sum of all values in a tree. What is the base case and what is the combine?

<details><summary>Answer</summary>
Base case: the empty tree sums to 0. Combine: this node's value plus the left sum plus the
right sum. Three lines, same skeleton as depth.
</details>

3. "Return the rightmost value on each row." BFS or DFS, and why?

<details><summary>Answer</summary>
BFS. The word "row" means you need whole levels at once, and BFS hands you one row at a time.
Keep the last value of each row.
</details>

## Common confusions, cleared

- **"How can a function call itself before it is finished?"** Each call gets its own fresh
  variables and its own smaller tree, and finishes as soon as the two below it do. Check the
  empty case and the one-node case by hand, check that your combine line is right assuming the
  children's answers are right, then stop tracing. That is the whole proof.
- **"Is a BST just 'left child smaller, right child bigger'?"** No. It is "everything in the
  left subtree smaller, everything in the right subtree bigger." A grandchild can break the rule
  while every parent-child pair looks fine. Pass the allowed range down.
- **"Why does level order need that `len(queue)` trick?"** When a row starts, the queue holds
  exactly that row. Its length tells you how many to pop before the next row begins. Without it,
  everything blurs into one flat list.
- **"Depth in nodes or edges?"** Depth here counts nodes, so one node has depth 1. Diameter
  counts edges, so two connected nodes have diameter 1. Say which one you mean out loud.

## What to do next

Open `LESSON.md` and read §2, the fully worked `max_depth`, and redo the table above with the
lesson's example until the flow of answers upward feels natural. Then read the "Recursive DFS
skeleton" at the top of §3. Then open `exercises.py` and do `max_depth` and `same_tree` with a
30-minute timer. When they pass, do `level_order` so you have written both a DFS and a BFS
before you go anywhere near a BST.
