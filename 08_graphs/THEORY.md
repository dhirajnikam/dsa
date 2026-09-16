# 08 · Graphs, explained from zero

Read this first if "BFS" or "union-find" sound like foreign words. When the city map below
feels obvious, move to `LESSON.md`, the dense reference. This file is the conversation with a
patient friend before you open the reference.

## In one sentence

A graph is a bunch of things and the connections between them, and every graph algorithm is a
way of walking those connections without going in circles.

## Start with something you already do

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

## Now the same thing with numbers

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

## The words people use

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

## Why the fast way is fast

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

## Try it in your head

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

## Common confusions, cleared

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

## What to do next

Open `LESSON.md` and read §1, the core idea, then §2, Number of Islands, which is the chalk
story on a grid. Then open `exercises.py` and do `num_islands` and `count_components` with a
timer. When they pass, read the BFS and Kahn's templates in §3 and try `can_finish_courses`,
the getting-dressed story in code.
