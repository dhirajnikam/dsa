# Phase 13: Graphs

**Goal:** spot a graph hiding in a grid or a prerequisite list, then pick BFS, DFS, topo sort, union-find, or Dijkstra and type it from memory.

## Key idea
A graph is nodes plus edges, stored as `graph[node] = [neighbors]`. A grid is already a graph: a cell's neighbors are the 4 cells around it. BFS explores in layers, so the first visit is the shortest path.
DFS is the tree recursion from Phase 11: mark `seen`, recurse into unseen neighbors. Use it for regions.

## Cheat sheet
```python
from collections import deque, defaultdict
graph = defaultdict(list)            # for u, v in edges: graph[u].append(v); graph[v].append(u)
q, seen = deque([start]), {start}                             # BFS: shortest path
while q:
    for _ in range(len(q)):                                   # one layer = one step
        for nxt in graph[q.popleft()]:
            if nxt not in seen: seen.add(nxt); q.append(nxt)  # mark when adding
q, order = deque(n for n in range(N) if indeg[n] == 0), []    # topo sort (Kahn)
while q:
    node = q.popleft(); order.append(node)
    for nxt in graph[node]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0: q.append(nxt)                     # len(order) < N: cycle
parent = list(range(N))                                       # union-find
def find(x): return x if parent[x] == x else find(parent[x])
def union(a, b):                                              # False = already joined = cycle
    ra, rb = find(a), find(b); parent[rb] = ra; return ra != rb
```

## When you see... use...
- "shortest path / fewest steps / minutes until" -> BFS (seed all sources at once if many)
- "count islands / regions / reachable cells" -> DFS from each unseen cell
- "prerequisites / order to take courses" -> topo sort; leftover nodes mean a cycle
- "connect these two / count groups / redundant edge" -> union-find
- "shortest path with weights" -> Dijkstra: heap of `(dist, node)`, skip stale entries

## Common mistakes
- Marking `seen` when popping instead of when pushing. You get duplicates in the queue.
- Adding both edge directions for a directed graph.
- Deep recursion on big grids hits Python's 1000 limit. Go iterative or raise it.
- Clone graph: store the copy in the map *before* recursing, or cycles loop forever.

## Problems
- `01_number_of_islands.py` — DFS flood fill, count starts
- `02_max_area_island.py` — DFS returns region size
- `03_clone_graph.py` — original-to-copy map
- `04_rotting_oranges.py` — multi-source BFS, layers are minutes
- `05_pacific_atlantic_water_flow.py` — search backwards from both oceans
- `06_course_schedule.py` — cycle check with Kahn
- `07_course_schedule_ii.py` — Kahn, return the order
- `08_number_of_connected_components.py` — union-find count
- `09_redundant_connection.py` — first edge whose union fails
- `10_network_delay_time.py` — Dijkstra, answer is max distance
- `11_cheapest_flights_k_stops.py` — Bellman-Ford, k+1 rounds
- `12_alien_dictionary.py` — edges from adjacent words, topo sort
