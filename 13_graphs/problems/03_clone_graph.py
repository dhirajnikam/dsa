"""
Problem: Clone Graph
Difficulty: Medium | Pattern: DFS/BFS with old->new map
Source: LeetCode 133

Given a reference to a node in a connected undirected graph, return a deep copy of the
graph. Each Node has an int val and a list of neighbors. Node values are unique 1..n.
Return None for an empty graph.

Example:
  adj = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]} -> a new graph with the same structure

Constraints:
  0 <= number of nodes <= 100
  No self-loops or repeated edges. The graph is connected.

Hints:
1. Keep a dict original -> copy. Create the copy BEFORE recursing into neighbors,
   otherwise cycles recurse forever.
2. clone(node): if node in seen, return seen[node]; else create copy, store, then append
   clone(nb) for each neighbor.
3. BFS works equally well: copy nodes as you discover them, wire neighbors as you dequeue.

Expected: O(V + E) time, O(V) space
"""
from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: "Optional[list[Node]]" = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build(adj: dict[int, list[int]]) -> Optional[Node]:
    """Build a graph from {val: [neighbor vals]}; return the node with the smallest val."""
    if not adj:
        return None
    nodes = {v: Node(v) for v in adj}
    for v, nbs in adj.items():
        nodes[v].neighbors = [nodes[u] for u in nbs]
    return nodes[min(adj)]


def serialize(node: Optional[Node]) -> dict[int, list[int]]:
    """Return {val: sorted neighbor vals} for every reachable node."""
    out, stack = {}, [node] if node else []
    while stack:
        cur = stack.pop()
        if cur.val in out:
            continue
        out[cur.val] = sorted(nb.val for nb in cur.neighbors)
        stack.extend(cur.neighbors)
    return out


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    raise NotImplementedError


if __name__ == "__main__":
    def check(adj):
        original = build(adj)
        copy = clone_graph(original)
        assert serialize(copy) == {v: sorted(n) for v, n in adj.items()}, 'Check: serialize(copy) == {v: sorted(n) for v, n in adj.items()}'
        if original is not None:
            assert copy is not original, 'Check: copy is not original'
            # no shared nodes between original and copy
            stack, seen_copy = [copy], set()
            while stack:
                cur = stack.pop()
                if id(cur) in seen_copy:
                    continue
                seen_copy.add(id(cur))
                stack.extend(cur.neighbors)
            stack, seen_orig = [original], set()
            while stack:
                cur = stack.pop()
                if id(cur) in seen_orig:
                    continue
                seen_orig.add(id(cur))
                stack.extend(cur.neighbors)
            assert not (seen_copy & seen_orig), 'Check: not (seen_copy & seen_orig)'

    check({1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]})
    check({1: []})
    check({})
    check({1: [2], 2: [1]})
    check({1: [2, 3], 2: [1, 3], 3: [1, 2]})
    check({i: [j for j in range(1, 8) if j != i] for i in range(1, 8)})
    print("ok")
