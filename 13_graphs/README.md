# Graphs: track both connections and visits

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Queues, recursion, sets, and heaps for weighted paths.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **graph** has vertices and edges. Edges may be directed or undirected and may carry weights. An adjacency list records neighbors. A grid can be a graph too: cells are vertices and legal moves are edges.

DFS explores deeply; BFS explores in layers. A visited set prevents repeating vertices and cycling forever. Marking a vertex when scheduled avoids repeatedly adding it to the frontier. Traversal with adjacency lists takes O(V+E) over the visited graph. Disconnected graphs require starting again from unvisited vertices.

BFS gives shortest paths in number of edges when edges have equal cost. Dijkstra handles non-negative edge weights; it does not support arbitrary negative weights. Some route tasks constrain stops, so the state may need both location and remaining budget rather than location alone.

**Topological ordering** puts prerequisites before dependents in a directed acyclic graph. Failure to process every vertex reveals a cycle. **Union-find** tracks merged components using representatives; path compression and rank/size heuristics keep operations efficient. Cloning a graph needs a map from each original node to its new node so shared neighbors stay shared.

## Walk through a small example

Roads connect A–B, A–C, and B–D, each one step. BFS from A visits layer 0 {A}, layer 1 {B, C}, then layer 2 {D}. If B–D costs 100 while A–C–D costs 3 in total, fewest roads and cheapest journey are different goals.

## Watch for

No visited tracking; forgetting disconnected components; using ordinary BFS for unequal weighted cost; collapsing different stop budgets into the same state.

## Your next small step

Open [number of islands](problems/01_number_of_islands.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 13/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Number of Islands](problems/01_number_of_islands.py)
- [Max Area of Island](problems/02_max_area_island.py)
- [Clone Graph](problems/03_clone_graph.py)
- [Rotting Oranges](problems/04_rotting_oranges.py)
- [Pacific Atlantic Water Flow](problems/05_pacific_atlantic_water_flow.py)
- [Course Schedule](problems/06_course_schedule.py)
- [Course Schedule II](problems/07_course_schedule_ii.py)
- [Number of Connected Components in an Undirected Graph](problems/08_number_of_connected_components.py)
- [Redundant Connection](problems/09_redundant_connection.py)
- [Network Delay Time](problems/10_network_delay_time.py)
- [Cheapest Flights Within K Stops](problems/11_cheapest_flights_k_stops.py)
- [Alien Dictionary](problems/12_alien_dictionary.py)

</details>
