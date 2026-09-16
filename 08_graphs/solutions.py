"""08 · Graphs — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""
import heapq
import sys
from collections import defaultdict, deque

from exercises import INF, GraphNode

sys.setrecursionlimit(10**6)

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])

    def sink(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"                       # mark visited by sinking
        for dr, dc in DIRS:
            sink(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                sink(r, c)
    return count
    # O(R*C) time; each cell scanned once and sunk at most once. O(R*C) stack worst case.


def max_area_island(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def area(r: int, c: int) -> int:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return 0
        grid[r][c] = 0
        return 1 + sum(area(r + dr, c + dc) for dr, dc in DIRS)

    return max((area(r, c) for r in range(rows) for c in range(cols)), default=0)
    # O(R*C) time and space.


def clone_graph(node: GraphNode | None) -> GraphNode | None:
    if node is None:
        return None
    copies: dict[GraphNode, GraphNode] = {}

    def clone(u: GraphNode) -> GraphNode:
        if u in copies:
            return copies[u]
        cp = GraphNode(u.val)
        copies[u] = cp                          # register BEFORE recursing, so cycles stop here
        cp.neighbors = [clone(v) for v in u.neighbors]
        return cp

    return clone(node)
    # O(V + E) time, O(V) space for the map (plus recursion).


def walls_and_gates(rooms: list[list[int]]) -> None:
    rows, cols = len(rooms), len(rooms[0])
    q = deque((r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)
    while q:                                    # multi-source BFS from every gate at once
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1  # first arrival is the nearest gate
                q.append((nr, nc))
    # O(R*C) time and space.


def rotting_oranges(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):                 # one level = one minute
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1
    # O(R*C) time and space.


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    rows, cols = len(heights), len(heights[0])
    pac: set[tuple[int, int]] = set()
    atl: set[tuple[int, int]] = set()

    def climb(r: int, c: int, seen: set[tuple[int, int]]) -> None:
        seen.add((r, c))                        # water flows down, so search UP from the ocean
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen
                    and heights[nr][nc] >= heights[r][c]):
                climb(nr, nc, seen)

    for c in range(cols):
        climb(0, c, pac)
        climb(rows - 1, c, atl)
    for r in range(rows):
        climb(r, 0, pac)
        climb(r, cols - 1, atl)
    return sorted([r, c] for r, c in pac & atl)
    # O(R*C) time: each ocean's DFS visits each cell at most once. O(R*C) space.


def surrounded_regions(board: list[list[str]]) -> list[list[str]]:
    rows, cols = len(board), len(board[0])

    def mark_safe(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
            return
        board[r][c] = "S"                       # border-connected: cannot be captured
        for dr, dc in DIRS:
            mark_safe(r + dr, c + dc)

    for r in range(rows):
        mark_safe(r, 0)
        mark_safe(r, cols - 1)
    for c in range(cols):
        mark_safe(0, c)
        mark_safe(rows - 1, c)
    for r in range(rows):
        for c in range(cols):
            board[r][c] = "O" if board[r][c] == "S" else "X"
    return board
    # O(R*C) time and space.


def _topo_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    adj: dict[int, list[int]] = defaultdict(list)
    indeg = [0] * num_courses
    for a, b in prerequisites:                  # b -> a : b before a
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    order: list[int] = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == num_courses else []
    # Kahn's algorithm. O(V + E) time and space.


def can_finish_courses(num_courses: int, prerequisites: list[list[int]]) -> bool:
    return len(_topo_order(num_courses, prerequisites)) == num_courses
    # Alternative: DFS with WHITE/GRAY/BLACK colors; meeting GRAY means a cycle.


def find_order_courses(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    return _topo_order(num_courses, prerequisites)


def valid_tree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:                     # a tree has exactly n - 1 edges
        return False
    uf = UnionFind(n)
    return all(uf.union(a, b) for a, b in edges)  # every edge must join two components
    # O(n α(n)). With n - 1 edges and no cycle, the graph is automatically connected.


def count_components(n: int, edges: list[list[int]]) -> int:
    uf = UnionFind(n)
    components = n
    for a, b in edges:
        if uf.union(a, b):
            components -= 1                     # a successful union merges two components
    return components
    # O((n + E) α(n)) time, O(n) space.


def redundant_connection(edges: list[list[int]]) -> list[int]:
    uf = UnionFind(len(edges) + 1)              # nodes are 1..n, and n == len(edges)
    for a, b in edges:
        if not uf.union(a, b):                  # endpoints already connected: this edge closes a cycle
            return [a, b]
    return []
    # O(E α(n)). Processing in order makes the LAST cycle-closing edge the one we return.


def word_ladder(begin: str, end: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end not in words:
        return 0
    q = deque([(begin, 1)])
    seen = {begin}
    while q:
        w, steps = q.popleft()
        if w == end:
            return steps
        for i in range(len(w)):                 # neighbors: every one-letter change
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nxt = w[:i] + ch + w[i + 1:]
                if nxt in words and nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, steps + 1))
    return 0
    # O(N * L * 26 * L) = O(N L^2): N words, L positions, 26 letters, L to build the string.


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    adj: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))
    dist = {k: 0}
    heap = [(0, k)]
    while heap:                                 # Dijkstra
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue                            # stale entry
        for v, w in adj[u]:
            if d + w < dist.get(v, float("inf")):
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return max(dist.values()) if len(dist) == n else -1
    # O((V + E) log V) time, O(V + E) space.


def cheapest_flights_k_stops(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(k + 1):                      # k stops = k + 1 edges = k + 1 rounds
        nxt = dist[:]                           # copy: a round may only extend last round's paths
        for u, v, w in flights:
            if dist[u] + w < nxt[v]:
                nxt[v] = dist[u] + w
        dist = nxt
    return dist[dst] if dist[dst] != float("inf") else -1
    # Bellman-Ford. O(k * E) time, O(n) space.


def min_cost_connect_points(points: list[list[int]]) -> int:
    n = len(points)
    in_tree = [False] * n
    heap = [(0, 0)]                             # (cost to attach, point index)
    total = added = 0
    while added < n:                            # Prim, lazy: pop until we hit a new point
        cost, i = heapq.heappop(heap)
        if in_tree[i]:
            continue
        in_tree[i] = True
        total += cost
        added += 1
        x1, y1 = points[i]
        for j in range(n):
            if not in_tree[j]:
                x2, y2 = points[j]
                heapq.heappush(heap, (abs(x1 - x2) + abs(y1 - y2), j))
    return total
    # O(n^2 log n) time, O(n^2) heap worst case. Kruskal on all n^2 edges: O(n^2 log n) too.


def alien_dictionary(words: list[str]) -> str:
    adj: dict[str, set[str]] = {c: set() for w in words for c in w}
    indeg = {c: 0 for c in adj}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in adj[x]:             # first difference gives one edge x -> y
                    adj[x].add(y)
                    indeg[y] += 1
                break
        else:
            if len(a) > len(b):                 # "abc" before "ab" is impossible
                return ""
    q = deque(c for c in adj if indeg[c] == 0)
    order: list[str] = []
    while q:                                    # Kahn's on letters
        c = q.popleft()
        order.append(c)
        for d in adj[c]:
            indeg[d] -= 1
            if indeg[d] == 0:
                q.append(d)
    return "".join(order) if len(order) == len(adj) else ""
    # O(total letters) to build edges, O(26 + E) for the sort.


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path halving
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:       # union by rank: shorter tree goes under taller
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)
    # Amortized O(α(n)) per operation, effectively constant.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
