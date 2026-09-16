# 08 · Graphs

**In one sentence.** A graph is things plus the connections between them, and every graph
algorithm is a way of walking those connections without going in circles.

**Why you care.** Google Maps routes you with Dijkstra. `pip install` orders packages with a
topological sort. Google puts a graph problem in most onsite loops, and Amazon asks the grid
problems (islands, rotting oranges) and course scheduling constantly.

## The idea, with a story

Picture a city map. Intersections are the *things*. Roads are the *connections*. You are at
one intersection and want the bakery.

**The ripple.** Drop a stone in a pond. The ripple reaches everything one step away, then two,
then three. Do that on the map: list every intersection one road away, then every unlisted one
two roads away, and so on. The first time the ripple touches the bakery, you know the fewest
roads to get there. That is BFS, and it is why BFS finds shortest paths.

**The maze walk.** Or put one hand on the wall and walk. Follow a road to its end. At a fork,
take the first turn. At a dead end, back up to the last fork and take the next turn. Deep
before wide. That is DFS. It finds *a* route and visits everything.

**The chalk.** Either way, mark an X at every intersection you reach. If you arrive somewhere
already marked, turn around. Without chalk, one loop keeps you walking forever. The chalk
marks are the "visited" set.

Roads of different lengths? Always expand the intersection closest so far in total distance.
That one change turns BFS into Dijkstra. Socks before shoes is a topological sort. Handshakes
merging friend groups at a party is union-find.

## The same story with numbers

A tiny map. Letters are intersections, lines are roads.

```
    A --- B --- D
    |
    C --- E
```

Run the ripple from A. The queue is the places waiting their turn, oldest first. Chalk goes
on when a place *enters* the queue.

| Step | Take from queue | Unchalked neighbours | Queue after | Distance from A |
|------|-----------------|----------------------|-------------|-----------------|
| 1 | A | B, C | B, C | A = 0 |
| 2 | B | D | C, D | B = 1 |
| 3 | C | E | D, E | C = 1 |
| 4 | D | none | E | D = 2 |
| 5 | E | none | empty | E = 2 |

Everything at distance 1 came out before anything at distance 2.

Pause and predict: add a road D–E. Does E's distance change? What does the chalk do when D
looks at E?

<details><summary>Answer</summary>
No. E was chalked at distance 2 (via C) before D's turn, so D skips it. The chalk stops E
from being counted twice with two different distances.
</details>

A grid is a graph in disguise. Each cell is an intersection. Its up, down, left, and right
neighbours are the roads.

## The anchor problem: Number of Islands

A grid of `"1"` (land) and `"0"` (water). An island is land connected up, down, left, or
right. Count the islands.

**Brute force.** Every cell must be looked at once, so O(rows × cols) is the floor. Say that.

**Insight.** Each unvisited land cell I meet is a *new* island. Flood-fill from it, sinking
every connected land cell, so I never count it again. The flood fill is DFS on the grid.

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def sink(r, c):                       # DFS: sink this cell and all connected land
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"                  # visited = sunk
        sink(r + 1, c); sink(r - 1, c); sink(r, c + 1); sink(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":         # first touch of a new island
                count += 1
                sink(r, c)
    return count
```

**Complexity.** O(rows × cols) time. O(rows × cols) space worst case for the recursion stack.

**What to say.** "Every land cell I reach for the first time starts a new island. I DFS from
it and sink all connected land so I never count it twice. Time and space are both
O(rows × cols). If depth is a concern, I switch to an explicit stack or a BFS deque."

## Templates you memorize

**BFS: shortest path when every edge costs 1.** Mark visited when you enqueue.
```python
from collections import deque

def bfs(start, adj):
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:             # chalk goes on at enqueue time
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
```
For "how many rounds," `for _ in range(len(q))` inside the `while` pops exactly one layer.
For "nearest gate for every cell," put all sources in the queue at distance 0 first.

**DFS on a grid.** Check bounds before touching the cell.
```python
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def dfs(r, c):
    if not (0 <= r < rows and 0 <= c < cols) or (r, c) in seen or grid[r][c] != target:
        return
    seen.add((r, c))
    for dr, dc in DIRS:
        dfs(r + dr, c + dc)
```

**Topological sort, Kahn's algorithm.** Nodes with no prerequisites go first. Fewer than `n`
in the order means a cycle.
```python
def topo_kahn(n, edges):                   # (u, v): u must come before v
    adj = defaultdict(list); indeg = [0] * n
    for u, v in edges:
        adj[u].append(v); indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []   # [] means cycle
```

**Union-Find.** "Are these two connected?" and "merge these groups," each near O(1).
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)); self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path compression
            x = self.parent[x]
        return x

    def union(self, a, b):                 # False if already connected
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        return True
```

**Dijkstra: shortest path with non-negative weights.** A min-heap of `(dist, node)`.
```python
import heapq

def dijkstra(n, adj, src):                 # adj[u] = [(v, w), ...]
    dist = [float("inf")] * n; dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:                    # stale entry, skip
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```
O((V + E) log V). For negative edges or "at most k stops," use Bellman-Ford instead: relax
every edge `k + 1` times, copying the array each round.

## When you see X, think Y

| You see | Think |
|---------|-------|
| grid, "connected", "island", "region" | grid DFS/BFS with 4 directions |
| "shortest path", "minimum steps", unweighted | BFS, level by level |
| "nearest X for every cell", "time until all are ..." | multi-source BFS, all sources at distance 0 |
| "prerequisites", "order to take/build" | Kahn's topological sort |
| "can it be finished", "is there a cycle" (directed) | Kahn's leftover nodes, or DFS with three colours |
| "is it a tree", "number of components", "redundant edge" | Union-Find |
| weighted, non-negative, "cheapest / fastest" | Dijkstra |
| "at most k stops", negative weights | Bellman-Ford, `k + 1` rounds |
| "words differing by one letter", "clone" | hidden graph; BFS, or DFS with an old-to-new map |

## Words you will hear

- **Node / edge.** One thing, one connection. `V` and `E` count them.
- **Directed / undirected.** One-way streets versus two-way.
- **Adjacency list.** Dict from node to its neighbours. The usual storage.
- **Visited set.** The chalk marks.
- **Queue / stack.** First in first out gives BFS. Last in first out gives DFS.
- **In-degree.** How many arrows point into a node. Its prerequisite count.
- **Connected component.** One friend group. Nodes that can all reach each other.
- **Relax.** Check whether this edge gives a shorter total to its far end, and update if so.

## Mistakes everyone makes once

- **Marking visited on dequeue instead of enqueue.** The same node enters the queue many
  times and dense graphs go O(V²). Mark when you add.
- **Indexing before the bounds check.** Check `0 <= nr < rows` before `grid[nr][nc]`.
- **Kahn's without the final count.** A cycle silently returns a partial order. Compare
  `len(order)` with `n`.
- **Adding an undirected edge once.** Add both directions or DFS misses half the graph.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO. `GraphNode`, `build_graph`, and
`to_adj_list` are helpers, already written.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `num_islands` | Medium | The anchor. Scan; each unvisited land cell starts a DFS that sinks the island. |
| 2 | `max_area_island` | Medium | Same DFS, but return `1 + sum of the four calls`. Track the max. |
| 3 | `clone_graph` | Medium | Dict old to new. Create the copy, store it, *then* recurse into neighbours. |
| 4 | `walls_and_gates` | Medium | Multi-source BFS from every gate. Only overwrite cells still holding INF. |
| 5 | `rotting_oranges` | Medium | Multi-source BFS from all rotten. Count levels. Fresh left means -1. |
| 6 | `pacific_atlantic` | Medium | DFS *uphill* from each ocean's border. Answer is the intersection. |
| 7 | `surrounded_regions` | Medium | DFS from border O's, mark them safe, flip the rest. |
| 8 | `can_finish_courses` | Medium | Kahn's. Fewer than `n` nodes in the order means a cycle. |
| 9 | `find_order_courses` | Medium | Same as 8, return the order. `[]` on a cycle. |
| 10 | `valid_tree` | Medium | Exactly `n - 1` edges and every union succeeds. |
| 11 | `count_components` | Medium | Start at `n`, subtract 1 per successful union. |
| 12 | `redundant_connection` | Medium | Union-Find in edge order. First edge whose ends are already connected. |
| 13 | `word_ladder` | Hard | BFS on words. Neighbours: change each position to each of 26 letters. |
| 14 | `network_delay_time` | Medium | Dijkstra from `k`. Answer is `max(dist)`; unreachable means -1. |
| 15 | `cheapest_flights_k_stops` | Medium | Bellman-Ford, `k + 1` rounds, copy the array each round. |
| 16 | `min_cost_connect_points` | Medium | Prim: heap of `(cost, point)`, skip points already in the tree. |
| 17 | `alien_dictionary` | Hard | Edge from the first differing letter of adjacent words. Kahn's on letters. |
| 18 | `UnionFind` | Medium | The template above, from memory. `union` returns whether it merged. |

Do 1 and 18 first, then 2 to 12 in order. 13 to 17 are for when those pass cold.
