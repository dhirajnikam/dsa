from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: "Optional[list[Node]]" = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build(adj):
    if not adj:
        return None
    nodes = {v: Node(v) for v in adj}
    for v, nbs in adj.items():
        nodes[v].neighbors = [nodes[u] for u in nbs]
    return nodes[min(adj)]


def serialize(node):
    out, stack = {}, [node] if node else []
    while stack:
        cur = stack.pop()
        if cur.val in out:
            continue
        out[cur.val] = sorted(nb.val for nb in cur.neighbors)
        stack.extend(cur.neighbors)
    return out


def clone_graph(node):
    # O(V + E) time, O(V) space
    # DFS with an original->copy map; register the copy before visiting neighbors so
    # cycles terminate.
    copies = {}

    def clone(n):
        if n in copies:
            return copies[n]
        c = copies[n] = Node(n.val)
        c.neighbors = [clone(nb) for nb in n.neighbors]
        return c

    return clone(node) if node else None
