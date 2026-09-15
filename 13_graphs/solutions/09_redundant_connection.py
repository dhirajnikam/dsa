def find_redundant_connection(edges):
    # O(n * alpha(n)) time, O(n) space
    # Union edges in order; the first edge whose endpoints already share a root closes the
    # single cycle and is the answer.
    parent = list(range(len(edges) + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return [a, b]
        parent[ra] = rb
    return []
