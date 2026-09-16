# 08 · Graphs

> A graph is just "things and the connections between them." Cities and roads, courses and
> prerequisites, cells and their neighbors. Almost every graph interview question is one of
> five algorithms wearing a costume. Learn the five, and learn to see through the costume.

**Interview frequency:** very high at Google, where a graph problem appears in most onsite
loops and is often the "hard" round. Amazon asks the grid problems (islands, rotting oranges)
and course scheduling constantly. This is the longest chapter for a reason.

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

A graph is a bunch of things and the connections between them, and every graph algorithm is a
way of walking those connections without going in circles.

### Start with something you already do

Picture a city map. Intersections are the *things*. Roads are the *connections*. You are at
one intersection and want the bakery.

**The ripple.** Drop a stone in a pond. The ripple reaches everything one step away, then two,
then three. Do that on the map: list every intersection one road away, then every unlisted one
two roads away, and so on. The first time the ripple touches the bakery, you know the fewest
roads to get there, because close places are reached before far ones. That is BFS, and it is
why BFS finds shortest paths.

**The maze walk.** Or put one hand on the wall and walk. Follow a road to its end. At a fork,
take the first turn. At a dead end, back up to the last fork and take the next turn. Deep
before wide. That is DFS. It finds *a* route, not the shortest, and it visits everything.

**The chalk.** Either way, you carry chalk and mark an X at every intersection you reach. If
you arrive somewhere already marked, you turn around. Without chalk, one loop in the city
keeps you walking forever. The chalk marks are the "visited" set.

**Getting dressed.** Socks before shoes, shirt before jacket. Socks and shirt can go in either
order. Listing clothes in an order that respects every "before" rule is a topological sort.
Course prerequisites are the same puzzle.

**Roads of different lengths.** The ripple assumes every road is one block. If roads differ,
always expand the intersection that is *closest so far* in total distance. That one change
turns BFS into Dijkstra.

**Handshakes.** Ten strangers at a party. Two shake hands and become one friend group. One of
them shakes with someone in another group, and the two groups merge. "Are these two in the
same group?" means checking whether they have the same group leader. That is union-find.

### Now the same thing with numbers

A tiny map. Letters are intersections, lines are roads.

```
    A --- B --- D
    |
    C --- E
```

Run the ripple from A. The "queue" is the list of places waiting their turn, oldest first.
Chalk goes on when a place *enters* the queue.

| Step | Take from queue | Unchalked neighbours | Queue after | Distance from A |
|------|-----------------|----------------------|-------------|-----------------|
| 1 | A | B, C | B, C | A = 0 |
| 2 | B | D | C, D | B = 1 |
| 3 | C | E | D, E | C = 1 |
| 4 | D | none | E | D = 2 |
| 5 | E | none | empty | E = 2 |

Visit order: A, B, C, D, E. Everything at distance 1 came out before anything at distance 2.
Pause and predict: add a road D–E. Does E's distance change? What does the chalk do when D
looks at E?

<details><summary>Answer</summary>
No. E was chalked at distance 2 (via C) before D's turn, so D skips it. The chalk stops E
from being counted twice with two different distances.
</details>

A grid is a graph in disguise. Each cell is an intersection, and its up, down, left, and
right neighbours are the roads. "Count the islands" means "count the friend groups of land
cells."

### The words people use

- **Graph.** Things plus connections. The map.
- **Node / vertex.** One thing. `V` is how many there are.
- **Edge.** One connection. `E` is how many there are.
- **Directed / undirected.** One-way streets versus two-way. "A is a prerequisite of B" is
  directed. "A and B are friends" is undirected.
- **Weighted.** Each road has a length or cost. Unweighted means every road counts as 1.
- **Adjacency list.** For each node, the list of its neighbours. A dictionary from node to
  list. The usual way to store a graph.
- **Adjacency matrix.** A square yes/no table for every pair of nodes. More memory. Only worth
  it when almost every pair is connected.
- **Neighbour.** A node one edge away.
- **Visited set.** The chalk marks.
- **BFS, breadth-first search.** The ripple. Uses a **queue**: first in, first out, like a
  line at a shop. Finds shortest paths when all edges cost 1.
- **DFS, depth-first search.** The maze walk. Uses a **stack**: last in, first out, like a
  pile of plates. Recursion is a hidden stack.
- **Frontier / level.** The nodes waiting in the queue are the frontier. One level is all
  nodes at the same distance: one ring of the ripple.
- **Multi-source BFS.** Drop several stones at once. Each cell's first touch is its distance
  to the *nearest* stone.
- **Connected component.** One friend group. Nodes that can all reach each other.
- **Cycle.** A loop. A path that returns to its start.
- **In-degree.** How many arrows point *into* a node. Its prerequisite count.
- **Topological sort.** An order that respects every "before" rule. Impossible if there is a
  cycle.
- **Kahn's algorithm.** Repeatedly take a node with in-degree 0 and lower the in-degree of
  everything it points to.
- **Three colours.** White is unvisited, gray is "on my current path," black is finished.
  Meeting gray means you walked in a circle.
- **Union-find / disjoint set union.** The friend-group tracker. `find` gives the leader;
  `union` merges two groups. **Path compression** and **union by rank** are two tricks that
  keep it near instant: point everyone straight at the leader, and hang the smaller group
  under the bigger one.
- **Dijkstra.** Shortest path with different non-negative road lengths. Uses a **min-heap**,
  a bag that always hands you the smallest item. To **relax** an edge is to check whether
  this road gives a shorter total to its far end and update if so.
- **Bellman-Ford.** Relax every edge, repeat `k` times. Slower, but survives negative weights
  and "at most k stops."
- **Minimum spanning tree (MST).** The cheapest set of roads that still connects everything.
  Prim and Kruskal build it.
- **O(V + E).** Touch every node once and every edge once. The cost of BFS and DFS.

### Why the fast way is fast

The slow way to answer "can A reach Z?" is to try every route, and routes explode. The fast
way visits each node and edge once, thanks to the chalk.

| Nodes | Edges (about 2 per node) | BFS or DFS work | Without chalk |
|-------|--------------------------|-----------------|---------------|
| 10 | 20 | about 30 | thousands |
| 1,000 | 2,000 | about 3,000 | astronomically many |
| 100,000 | 200,000 | about 300,000 | never finishes |

Dijkstra pays a little for the heap, roughly (V + E) × log V. Still a blink.

The trade-off: memory for the visited set and the queue, up to one entry per node, plus one
setup pass to build the adjacency list. You pay that to never walk the same road twice.

### Try it in your head

1. On the tiny map, run the maze walk (DFS) from A, taking neighbours alphabetically. Visit
   order?

<details><summary>Answer</summary>
A, B, D, then back to A, then C, E. So A, B, D, C, E. D came before C: DFS ignores distance.
</details>

2. Courses: 1 needs 0, 2 needs 0, 3 needs 1 and 2. In-degrees, and which course goes first?

<details><summary>Answer</summary>
0 has 0, 1 has 1, 2 has 1, 3 has 2. Only course 0 is free. After it, courses 1 and 2 drop to 0.
</details>

3. Five strangers. Then 0 shakes with 1, 2 shakes with 3, 1 shakes with 3. How many groups?

<details><summary>Answer</summary>
Start at 5. Each handshake between different groups merges two: 5 → 4 → 3 → 2. Groups are
{0, 1, 2, 3} and {4}.
</details>

### Common confusions, cleared

- **"BFS and DFS look identical. What differs?"** One line. BFS takes from the front of the
  waiting list, DFS from the back. Which end you take from decides whether you spread out or
  dive deep.
- **"Chalk when I add a node to the queue, or when I take it out?"** When you add it. If you
  wait, the same node can be added by several neighbours and the queue swells. Everyone gets
  this wrong once.
- **"Why not BFS when roads have lengths?"** BFS counts roads, not distance. Two short roads
  can beat one long one, and BFS would pick the long one. Dijkstra's heap always picks the
  smallest *total*.
- **"Union-find or DFS for counting components?"** Both work. Union-find shines when edges
  arrive one at a time or the question is "does this edge close a loop?" DFS is simpler when
  you already have the whole graph.

### What to do next

Scroll down to Part 2 and read §1, the core idea, then Part 2 §2, Number of Islands, which is the chalk
story on a grid. Then open `exercises.py` and do `num_islands` and `count_components` with a
timer. When they pass, read the BFS and Kahn's templates in Part 2 §3 and try `can_finish_courses`,
the getting-dressed story in code.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** Google Maps finds your fastest route by running
Dijkstra over a graph of intersections and roads. PageRank, the idea that built Google,
treats the web as a graph of pages and links. Amazon routes packages through a graph of
warehouses and roads, and its warehouse robots path-find on a grid graph. When you run
`pip install` or `npm install`, the tool topologically sorts a dependency graph so nothing is
built before what it needs. Friend suggestions and "people also bought" are walks through a
graph of people and products.

**The analogy.** A city map. Intersections are nodes, roads are edges, and every algorithm
here is a way of exploring the map without going in circles. BFS is the ripple from a stone
dropped in water: it reaches everything one block away, then two, then three, so the first
time it touches a place is the shortest way there. DFS is walking a maze with one hand on the
wall: follow a corridor to its end, back up to the last fork, take the next turn. Dijkstra is
BFS where some roads are slower, so you always step onto the closest place not yet reached.

**How it works, in plain words.** Every algorithm here does two things: look at a node's
neighbors, and remember where you have been. The visited set is the memory. Without it you
loop forever; with it, every node and edge is touched once, which is why the complexity is
almost always O(V + E). What differs is the container that decides which node comes next. A
queue gives BFS. A stack, or recursion, gives DFS. A min-heap keyed by distance gives
Dijkstra. Kahn's topological sort is BFS where a node enters the queue only when all its
prerequisites are done.

**What learning this will feel like.** Halfway through this chapter, BFS, DFS, topological
sort, Union-Find, Dijkstra, and Bellman-Ford will feel like six unrelated things to memorize.
That feeling is normal, and it is wrong. Keep going until the aha arrives: they are one loop
with a different container, and "hidden graph" problems like Word Ladder become easy once you
ask "what are my nodes, what are my edges." The bug everyone writes once is marking a node
visited when it leaves the queue instead of when it enters. It still works on small inputs,
then quietly goes O(V²) on a dense one. Mark on enqueue.

**You will know you have it when** "minimum number of steps" makes you reach for a deque
before you finish reading, and a grid of cells looks like nodes with four neighbors rather
than a matrix.

### 1. The core idea

Everything in this chapter is "visit every node reachable from here, without visiting one
twice." The data structure you use to decide *which node next* is the whole difference:

```
BFS: queue                        DFS: stack (or recursion)
visit in rings of distance        go deep, come back, go deep again
finds SHORTEST path (unweighted)  finds ANY path, detects cycles, orders things

      A                                 A
    / | \          BFS order            |           DFS order
   B  C  D         A B C D E F          B           A B E F C D
   |     |                              |
   E     F                              E ...
```

Both are O(V + E): every vertex enters the queue or stack once, every edge is looked at once
(twice for undirected). Say that sentence in interviews. It is the complexity of nearly
everything here.

The three questions to ask of any graph problem:

1. **What are the nodes and edges?** Often they are hidden. In Word Ladder the nodes are
   words and the edges are one-letter changes. In Alien Dictionary the nodes are letters.
2. **Directed or undirected? Weighted or not?** Unweighted shortest path is BFS. Weighted with
   non-negative edges is Dijkstra. Negative edges or "at most k steps" is Bellman-Ford.
3. **What am I asked?** Reachability or counting components: DFS/BFS/Union-Find. Shortest
   path: BFS/Dijkstra. Ordering with dependencies: topological sort. Cycle: DFS colors or
   Kahn's leftover nodes.

#### Representations

```python
from collections import defaultdict

# adjacency list from an edge list (the default; O(V + E) space)
adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)          # drop this line for a directed graph

# a grid IS a graph: each cell is a node, edges go to the 4 neighbors
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
for dr, dc in DIRS:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        ...
```

An adjacency matrix (`n × n` of booleans) is O(V²) space and only worth it for dense graphs
or when the problem hands you one. `defaultdict(list)` means a node with no outgoing edges
is safe to look up. Always ask: are node labels `0..n-1` (use a list) or arbitrary (use a dict)?

### 2. Anchor problem: Number of Islands, fully worked

**Problem.** A grid of `"1"` (land) and `"0"` (water). An island is a group of land cells
connected up, down, left, or right. Count the islands.

**Understand.** Diagonals do not connect. The grid can be modified? Ask. If yes, we can sink
visited land in place and skip a visited set. Empty grid → 0. All water → 0.

**Examples.**

```
1 1 0 0 0
1 1 0 0 0       → 3 islands
0 0 1 0 0
0 0 0 1 1
```

`[["1"]] → 1`. `[["0"]] → 0`.

**Brute force.** There is no meaningful brute force that is worse; the natural idea is already
optimal. Say that: "Every cell must be looked at at least once, so O(rows × cols) is a lower
bound. I will hit it."

**Insight.** Each time I meet a land cell I have not visited, that is a *new* island. I then
flood-fill from it, marking every connected land cell as visited so I never count it again.
The flood fill is DFS on the grid graph.

**Code.**

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def sink(r, c):                              # DFS: mark this cell and all connected land
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"                         # visited := sunk
        sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                sink(r, c)
    return count
```

**Test trace.** On the 4×5 grid above: (0,0) is "1" → count=1, sink floods (0,0),(0,1),(1,0),(1,1)
to "0". Scan continues; nothing until (2,2) → count=2, sink one cell. Then (3,3) → count=3,
floods (3,3),(3,4). Every remaining cell is "0". Return 3. ✓

**Complexity.** O(rows × cols) time: each cell is visited by the scan once and by `sink` at
most once. O(rows × cols) space in the worst case for the recursion stack (a snake-shaped
island). If asked to avoid mutating the input, use a `visited` set: same complexity.

**What to say out loud.** "Every land cell I reach for the first time in the scan starts a new
island. I DFS from it and mark all connected land as visited so I do not count it twice.
Time and space are both O(rows × cols). If recursion depth is a concern I can make the DFS
iterative with an explicit stack, or use BFS with a deque."

### 3. Patterns & templates in this chapter

#### BFS: shortest path in an unweighted graph

The queue holds the frontier. Mark visited **when you enqueue**, not when you dequeue, or
the same node enters the queue many times. Track distance by level or by storing it in the
queue tuple.

```python
from collections import deque

def bfs(start, adj):
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:              # visited check at enqueue time
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
```

Level-by-level form (when you need "how many rounds"): `for _ in range(len(q))` inside the
`while` pops exactly one layer.

#### Multi-source BFS

Put **all** sources in the queue at distance 0 before you start. The first time a cell is
reached, that is its true distance to the nearest source. Rotting Oranges, Walls and Gates,
"distance to nearest 0." One BFS instead of one per source: O(V + E) instead of O(V × (V + E)).

#### DFS, recursive and iterative

```python
def dfs(u, adj, seen):                     # recursive
    seen.add(u)
    for v in adj[u]:
        if v not in seen:
            dfs(v, adj, seen)

def dfs_iter(start, adj):                  # iterative, same visiting order as recursion
    seen = {start}
    stack = [start]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
```

Python's default recursion limit is 1000. A 1000×1000 grid can recurse a million deep. Write
`import sys; sys.setrecursionlimit(10**6)` at the top, or go iterative. Mention this; it shows
depth.

#### Topological sort, Kahn's algorithm (BFS with in-degrees)

Nodes with in-degree 0 have no prerequisites: they can go first. Remove one, decrement its
children's in-degrees, and any child that hits 0 is now free. If you finish with fewer than
`n` nodes in the order, there is a cycle.

```python
def topo_kahn(n, edges):                   # edges: (u, v) means u must come before v
    adj = defaultdict(list)
    indeg = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []  # [] means cycle
```

#### Topological sort, DFS with three colors (cycle detection)

WHITE = unvisited, GRAY = on the current path, BLACK = finished. Meeting a GRAY node means
you walked in a circle. Appending a node when it turns BLACK gives reverse topological order.

```python
WHITE, GRAY, BLACK = 0, 1, 2

def topo_dfs(n, adj):
    color = [WHITE] * n
    order = []

    def visit(u):                          # returns False on cycle
        if color[u] == GRAY:
            return False
        if color[u] == BLACK:
            return True
        color[u] = GRAY
        for v in adj[u]:
            if not visit(v):
                return False
        color[u] = BLACK
        order.append(u)                    # post-order
        return True

    for u in range(n):
        if not visit(u):
            return []
    return order[::-1]
```

For an **undirected** graph, cycle detection is simpler: DFS with a `parent` argument, and
any visited neighbor that is not the parent means a cycle. Or use Union-Find: an edge whose
endpoints are already connected closes a cycle.

#### Union-Find (Disjoint Set Union)

Answers "are these two connected?" and "merge these two groups" in near-O(1) each. Two
optimizations make it fast: **path compression** (point every node on the way up straight at
the root) and **union by rank** (attach the shorter tree under the taller one). Together they
give amortized O(α(n)), which is effectively constant.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n                     # number of components

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path halving
            x = self.parent[x]
        return x

    def union(self, a, b):                 # returns False if already connected
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)
```

Use it for: number of components, "is this a tree" (`n - 1` edges and every union succeeds),
the redundant edge, Kruskal's MST, and anything where edges arrive over time.

#### Dijkstra: shortest path with non-negative weights

BFS assumes every edge costs 1. With weights, the nearest unvisited node is not necessarily
the next one in the queue, so use a **min-heap of `(dist, node)`**. Pop the smallest; if it
is stale (we already have a better distance for that node), skip it; otherwise relax its edges.

```python
import heapq

def dijkstra(n, adj, src):                 # adj[u] = [(v, w), ...]
    dist = [float("inf")] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:                    # stale entry: a shorter path was already found
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

O((V + E) log V). **Why it fails with negative edges:** Dijkstra commits to a node's distance
when it pops it, assuming no later path can be shorter. A negative edge can make a later path
shorter, so the commitment is wrong. That is what Bellman-Ford is for.

#### Bellman-Ford: k rounds of relaxation

Relax every edge, `k` times. After round `i`, `dist[v]` is the cheapest path to `v` using at
most `i` edges. "At most k stops" means at most `k + 1` edges, so run `k + 1` rounds. Copy the
array each round so a round only uses paths from the previous round (otherwise one round can
chain many edges and break the "at most i edges" invariant).

```python
def bellman_ford(n, edges, src, rounds):   # edges: (u, v, w)
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(rounds):
        nxt = dist[:]
        for u, v, w in edges:
            if dist[u] + w < nxt[v]:
                nxt[v] = dist[u] + w
        dist = nxt
    return dist
```

O(rounds × E). Handles negative edges. With `n - 1` rounds it gives true shortest paths; an
`n`-th round that still improves something means a negative cycle.

#### Minimum spanning tree: Prim and Kruskal

Connect every node with the least total edge weight. **Prim** grows one tree: a heap of edges
leaving the tree, always take the cheapest edge to a node not yet in the tree. O(E log V).
**Kruskal** sorts all edges and adds each one whose endpoints are not yet connected
(Union-Find). O(E log E). For "connect all points, Manhattan distance," the graph is complete
(E = n²) and Prim with a lazy heap is the usual answer.

```python
def prim(n, adj):                          # adj[u] = [(w, v), ...]
    seen = {0}
    heap = list(adj[0])
    heapq.heapify(heap)
    total = 0
    while heap and len(seen) < n:
        w, v = heapq.heappop(heap)
        if v in seen:
            continue
        seen.add(v)
        total += w
        for edge in adj[v]:
            if edge[1] not in seen:
                heapq.heappush(heap, edge)
    return total
```

#### Cloning a graph

Recurse with a dict `old → new`. Create the copy before recursing into neighbors so a cycle
finds the copy already in the dict and stops. Trees are the special case with no cycle.

### 4. Recognition cues

| You see | Think |
|---------|-------|
| grid of cells, "connected", "island", "region" | grid DFS/BFS with 4 directions; mark visited by mutating or a set |
| "shortest path", "minimum steps", "fewest moves", unweighted | BFS; level-by-level if you need the count |
| "nearest X for every cell", "time until all are ..." | multi-source BFS: enqueue every source at distance 0 |
| "prerequisites", "dependencies", "order to take/build" | topological sort (Kahn's); leftover nodes mean a cycle |
| "can it be finished", "is there a cycle" (directed) | Kahn's, or DFS with three colors |
| "is it a tree", "number of connected components", "redundant edge" | Union-Find, or DFS counting components |
| weighted edges, non-negative, "cheapest / fastest" | Dijkstra with a heap of `(dist, node)` |
| "at most k stops / edges", or negative weights | Bellman-Ford, `k + 1` rounds with a copied array |
| "connect all points with minimum total cost" | MST: Prim (dense) or Kruskal (edge list) |
| "words that differ by one letter", "valid transformation" | hidden graph; nodes are words, BFS for shortest chain |
| "order of letters from a sorted dictionary" | edges from adjacent words' first difference, then topological sort |
| "deep copy", "clone" | DFS with an `old → new` map |

### 5. Pitfalls

- **Marking visited on dequeue instead of enqueue.** The same node enters the queue multiple
  times; on dense graphs this blows up to O(V²). Mark when you add.
- **Forgetting bounds checks** on grids, or checking them after indexing. Check `0 <= nr < rows`
  before touching `grid[nr][nc]`.
- **Recursion depth.** A 300×300 grid can recurse 90,000 deep. Raise the limit or go iterative.
- **Kahn's without the final count.** If a cycle exists you silently return a partial order.
  Always compare `len(order)` with `n`.
- **Dijkstra without the stale check** still works but does extra work. Dijkstra with negative
  edges is simply wrong. Say why.
- **Bellman-Ford relaxing in place** lets one round chain several edges and breaks the
  "at most k stops" guarantee. Copy the array.
- **Union-Find without compression** degrades to O(n) per `find`. Write the compression line;
  it is one line.
- **Undirected edges added once.** Add both directions, or your DFS misses half the graph.
- **Word Ladder by comparing every pair** of words is O(N² × L). Use the wildcard-pattern trick
  (`h*t`) to find neighbors in O(L²) per word, or just try all 26 letters per position.
- **Alien Dictionary: a prefix listed after its extension** (`["abc", "ab"]`) is invalid. And
  letters that never appear in an edge must still appear in the output.

### 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|----------|-----------|----------|----------|
| 1 | `num_islands` | Medium | Amazon, Google | The anchor. Scan; each unvisited land cell starts a DFS that sinks the island. |
| 2 | `max_area_island` | Medium | Amazon, Google | Same DFS, but return `1 + sum of the four recursive calls`. Track the max. |
| 3 | `clone_graph` | Medium | Google, Amazon | Dict `old → new`. Create the copy, store it, *then* recurse into neighbors. |
| 4 | `walls_and_gates` | Medium | Google | Multi-source BFS from every gate. Only overwrite cells that still hold INF. |
| 5 | `rotting_oranges` | Medium | Amazon | Multi-source BFS from all rotten. Count levels. Any fresh left at the end → -1. |
| 6 | `pacific_atlantic` | Medium | Google | Reverse the flow: DFS *uphill* from each ocean's border. Answer is the intersection. |
| 7 | `surrounded_regions` | Medium | Google, Amazon | Any O touching the border cannot be captured. DFS from border O's, mark them safe, flip the rest. |
| 8 | `can_finish_courses` | Medium | Amazon, Google | Kahn's. Finished with fewer than `n` nodes means a cycle. |
| 9 | `find_order_courses` | Medium | Amazon, Google | Same as 8, but return the order. Return `[]` on a cycle. |
| 10 | `valid_tree` | Medium | Google | A tree has exactly `n - 1` edges and is connected. Union-Find: every union must succeed. |
| 11 | `count_components` | Medium | Amazon, Google | Union-Find: start at `n`, subtract 1 per successful union. Or DFS from each unvisited node. |
| 12 | `redundant_connection` | Medium | Google | Union-Find in edge order. The first edge whose endpoints are already connected is the answer. |
| 13 | `word_ladder` | Hard | Amazon, Google | BFS on words. Neighbors: change each position to each of 26 letters and check the set. |
| 14 | `network_delay_time` | Medium | Amazon | Dijkstra from `k`. Answer is `max(dist)`; if any node is unreached, -1. |
| 15 | `cheapest_flights_k_stops` | Medium | Amazon, Google | Bellman-Ford, `k + 1` rounds, copy the array each round. |
| 16 | `min_cost_connect_points` | Medium | Google | Prim with a heap of `(cost, point)`. Manhattan distance. Skip points already in the tree. |
| 17 | `alien_dictionary` | Hard | Google, Amazon | Edge from the first differing letter of each adjacent pair. Kahn's on letters. Prefix-after-word → `""`. |
| 18 | `UnionFind` | Medium | Google | The template from §3, from memory. `union` returns whether it merged anything. |

Solve 1–12 in order. 13–18 are the stretch set; 18 is short and unlocks 10, 11, 12, 16, so if
you are stuck on those, write 18 first.
