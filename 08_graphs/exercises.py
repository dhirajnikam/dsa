"""08 · Graphs — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
"""
import sys
from collections import deque

sys.setrecursionlimit(10**6)

INF = 2**31 - 1


class GraphNode:
    """Node of an undirected graph: an integer value and a list of neighbor nodes."""

    def __init__(self, val: int = 0, neighbors: list["GraphNode"] | None = None) -> None:
        self.val = val
        self.neighbors: list[GraphNode] = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return f"GraphNode({self.val}, -> {[n.val for n in self.neighbors]})"


def build_graph(adj_list: list[list[int]]) -> GraphNode | None:
    """Build a connected undirected graph from a 1-indexed adjacency list.
    adj_list[i] lists the neighbor values of node i + 1. Returns node 1, or None if empty.
    [[2, 4], [1, 3], [2, 4], [1, 3]] -> a square 1-2-3-4-1
    """
    if not adj_list:
        return None
    nodes = [GraphNode(i + 1) for i in range(len(adj_list))]
    for i, nbrs in enumerate(adj_list):
        nodes[i].neighbors = [nodes[v - 1] for v in nbrs]
    return nodes[0]


def to_adj_list(node: GraphNode | None) -> list[list[int]]:
    """Inverse of build_graph: BFS from node, return the 1-indexed adjacency list."""
    if node is None:
        return []
    seen: dict[int, GraphNode] = {node.val: node}
    q = deque([node])
    while q:
        u = q.popleft()
        for v in u.neighbors:
            if v.val not in seen:
                seen[v.val] = v
                q.append(v)
    n = max(seen)
    return [[nb.val for nb in seen[i].neighbors] if i in seen else [] for i in range(1, n + 1)]


def num_islands(grid: list[list[str]]) -> int:
    """Count groups of "1" cells connected up/down/left/right. You may modify the grid.
    [["1","1","0"],["0","1","0"],["0","0","1"]] -> 2 ; [["0"]] -> 0 ; [] -> 0
    """
    raise NotImplementedError


def max_area_island(grid: list[list[int]]) -> int:
    """Largest number of cells in any 4-directionally connected group of 1s. 0 if none.
    [[0,1,0],[1,1,0],[0,0,1]] -> 3 ; [[0,0]] -> 0
    """
    raise NotImplementedError


def clone_graph(node: GraphNode | None) -> GraphNode | None:
    """Return a deep copy of the connected undirected graph reachable from node.
    No node object in the result may be a node of the input. None -> None.
    build_graph([[2],[1]]) -> a new two-node graph with the same shape
    """
    raise NotImplementedError


def walls_and_gates(rooms: list[list[int]]) -> None:
    """rooms holds -1 (wall), 0 (gate), or INF (empty). Fill every empty cell IN PLACE with the
    distance to its nearest gate (4-directional moves, cannot pass walls). Unreachable stays INF.
    [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
      -> [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
    """
    raise NotImplementedError


def rotting_oranges(grid: list[list[int]]) -> int:
    """0 empty, 1 fresh, 2 rotten. Each minute every rotten orange rots its 4 neighbors.
    Return minutes until no fresh orange remains, or -1 if impossible. No fresh -> 0.
    [[2,1,1],[1,1,0],[0,1,1]] -> 4 ; [[2,1,1],[0,1,1],[1,0,1]] -> -1 ; [[0,2]] -> 0
    """
    raise NotImplementedError


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    """Water flows from a cell to a 4-neighbor of equal or lower height. The Pacific touches
    the top and left edges, the Atlantic the bottom and right. Return every [r, c] from which
    water can reach both oceans, sorted.
    [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
      -> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]] ; [[1]] -> [[0,0]]
    """
    raise NotImplementedError


def surrounded_regions(board: list[list[str]]) -> list[list[str]]:
    """Flip every "O" that is NOT 4-connected to an "O" on the border into "X", in place.
    Return the board.
    [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
      -> [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    """
    raise NotImplementedError


def can_finish_courses(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """Courses 0..num_courses-1. [a, b] means you must take b before a. Can all be finished?
    2, [[1,0]] -> True ; 2, [[1,0],[0,1]] -> False ; 3, [] -> True
    """
    raise NotImplementedError


def find_order_courses(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """Return any order in which all courses can be taken, or [] if impossible.
    2, [[1,0]] -> [0, 1] ; 4, [[1,0],[2,0],[3,1],[3,2]] -> [0,1,2,3] or [0,2,1,3]
    """
    raise NotImplementedError


def valid_tree(n: int, edges: list[list[int]]) -> bool:
    """Do the undirected edges on nodes 0..n-1 form exactly one tree (connected, no cycle)?
    5, [[0,1],[0,2],[0,3],[1,4]] -> True ; 5, [[0,1],[1,2],[2,3],[1,3],[1,4]] -> False
    1, [] -> True
    """
    raise NotImplementedError


def count_components(n: int, edges: list[list[int]]) -> int:
    """Number of connected components in an undirected graph on nodes 0..n-1.
    5, [[0,1],[1,2],[3,4]] -> 2 ; 5, [[0,1],[1,2],[2,3],[3,4]] -> 1 ; 3, [] -> 3
    """
    raise NotImplementedError


def redundant_connection(edges: list[list[int]]) -> list[int]:
    """A tree on nodes 1..n plus exactly one extra edge. Return the edge whose removal leaves a
    tree; if several qualify, the one that appears last in edges.
    [[1,2],[1,3],[2,3]] -> [2,3] ; [[1,2],[2,3],[3,4],[1,4],[1,5]] -> [1,4]
    """
    raise NotImplementedError


def word_ladder(begin: str, end: str, word_list: list[str]) -> int:
    """Shortest chain begin -> ... -> end where each step changes one letter and every
    intermediate word (and end) is in word_list. Return the number of words in the chain
    including both ends, or 0 if none.
    "hit", "cog", ["hot","dot","dog","lot","log","cog"] -> 5
    "hit", "cog", ["hot","dot","dog","lot","log"] -> 0
    """
    raise NotImplementedError


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    """Directed weighted edges [u, v, w] on nodes 1..n. A signal leaves k at time 0.
    Return the time when every node has received it, or -1 if some node never does.
    [[2,1,1],[2,3,1],[3,4,1]], 4, 2 -> 2 ; [[1,2,1]], 2, 2 -> -1
    """
    raise NotImplementedError


def cheapest_flights_k_stops(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    """Flights [u, v, price]. Cheapest price from src to dst using at most k intermediate
    stops (k + 1 edges), or -1.
    4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1 -> 700
    3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1 -> 200 ; same, k=0 -> 500
    """
    raise NotImplementedError


def min_cost_connect_points(points: list[list[int]]) -> int:
    """Cost to connect two points is their Manhattan distance |x1-x2| + |y1-y2|.
    Minimum total cost to make every point reachable from every other (an MST).
    [[0,0],[2,2],[3,10],[5,2],[7,0]] -> 20 ; [[3,12],[-2,5],[-4,1]] -> 18 ; [[0,0]] -> 0
    """
    raise NotImplementedError


def alien_dictionary(words: list[str]) -> str:
    """words is sorted under some unknown alphabet. Return the letters in that alphabet's order
    (any valid order if several). Return "" if no order is consistent with the input.
    ["wrt","wrf","er","ett","rftt"] -> "wertf" ; ["z","x"] -> "zx" ; ["z","x","z"] -> ""
    ["abc","ab"] -> ""  (a word cannot come after its own extension)
    """
    raise NotImplementedError


class UnionFind:
    """Disjoint sets over 0..n-1 with path compression and union by rank.
    union(a, b) returns True if it merged two different sets, False if already together.
    connected(a, b) asks whether a and b share a set.
    """

    def __init__(self, n: int) -> None:
        raise NotImplementedError

    def find(self, x: int) -> int:
        raise NotImplementedError

    def union(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def connected(self, a: int, b: int) -> bool:
        raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_num_islands():
    g = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(g) == 3
    assert num_islands([["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]]) == 2
    assert num_islands([["0"]]) == 0
    assert num_islands([]) == 0
    assert num_islands([["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]]) == 5


def _t_02_max_area_island():
    assert max_area_island([[0, 1, 0], [1, 1, 0], [0, 0, 1]]) == 3
    assert max_area_island([[0, 0]]) == 0
    assert max_area_island([[1, 1], [1, 1]]) == 4
    g = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    assert max_area_island(g) == 6


def _t_03_clone_graph():
    for adj in ([[2, 4], [1, 3], [2, 4], [1, 3]], [[]], [[2], [1]]):
        src = build_graph(adj)
        cp = clone_graph(src)
        assert to_adj_list(cp) == adj, to_adj_list(cp)
        # every node in the copy must be a new object
        originals = set()
        stack = [src]
        while stack:
            u = stack.pop()
            if id(u) in originals:
                continue
            originals.add(id(u))
            stack.extend(u.neighbors)
        stack = [cp]
        seen = set()
        while stack:
            u = stack.pop()
            if id(u) in seen:
                continue
            seen.add(id(u))
            assert id(u) not in originals, "copy shares a node with the original"
            stack.extend(u.neighbors)
    assert clone_graph(None) is None


def _t_04_walls_and_gates():
    rooms = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]
    walls_and_gates(rooms)
    assert rooms == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]], rooms
    rooms = [[INF, -1], [-1, INF]]
    walls_and_gates(rooms)
    assert rooms == [[INF, -1], [-1, INF]]
    rooms = [[0]]
    walls_and_gates(rooms)
    assert rooms == [[0]]


def _t_05_rotting_oranges():
    assert rotting_oranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert rotting_oranges([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert rotting_oranges([[0, 2]]) == 0
    assert rotting_oranges([[1]]) == -1
    assert rotting_oranges([[0]]) == 0


def _t_06_pacific_atlantic():
    h = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    assert pacific_atlantic(h) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert pacific_atlantic([[1]]) == [[0, 0]]
    assert pacific_atlantic([[1, 1], [1, 1]]) == [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert pacific_atlantic([[1, 2, 3], [8, 9, 4], [7, 6, 5]]) == [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]


def _t_07_surrounded_regions():
    b = [list("XXXX"), list("XOOX"), list("XXOX"), list("XOXX")]
    assert surrounded_regions(b) == [list("XXXX"), list("XXXX"), list("XXXX"), list("XOXX")]
    assert surrounded_regions([["X"]]) == [["X"]]
    assert surrounded_regions([["O"]]) == [["O"]]
    b = [list("OOO"), list("OXO"), list("OOO")]
    assert surrounded_regions(b) == [list("OOO"), list("OXO"), list("OOO")]
    b = [list("XXX"), list("XOX"), list("XXX")]
    assert surrounded_regions(b) == [list("XXX"), list("XXX"), list("XXX")]


def _t_08_can_finish_courses():
    assert can_finish_courses(2, [[1, 0]]) is True
    assert can_finish_courses(2, [[1, 0], [0, 1]]) is False
    assert can_finish_courses(3, []) is True
    assert can_finish_courses(4, [[1, 0], [2, 1], [3, 2], [1, 3]]) is False
    assert can_finish_courses(1, []) is True


def _is_topo_order(order, n, prereqs):
    if sorted(order) != list(range(n)):
        return False
    pos = {c: i for i, c in enumerate(order)}
    return all(pos[b] < pos[a] for a, b in prereqs)


def _t_09_find_order_courses():
    assert find_order_courses(2, [[1, 0]]) == [0, 1]
    got = find_order_courses(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert _is_topo_order(got, 4, [[1, 0], [2, 0], [3, 1], [3, 2]]), got
    assert find_order_courses(2, [[1, 0], [0, 1]]) == []
    assert sorted(find_order_courses(3, [])) == [0, 1, 2]
    assert find_order_courses(1, []) == [0]


def _t_10_valid_tree():
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    assert valid_tree(1, []) is True
    assert valid_tree(4, [[0, 1], [2, 3]]) is False           # disconnected
    assert valid_tree(3, [[0, 1], [1, 2], [2, 0]]) is False   # cycle, right edge count


def _t_11_count_components():
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    assert count_components(3, []) == 3
    assert count_components(1, []) == 1
    assert count_components(4, [[0, 1], [1, 0], [2, 3]]) == 2


def _t_12_redundant_connection():
    assert redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    assert redundant_connection([[1, 2], [2, 3], [1, 3]]) == [1, 3]
    assert redundant_connection([[1, 2], [1, 2]]) == [1, 2]


def _t_13_word_ladder():
    assert word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert word_ladder("a", "c", ["a", "b", "c"]) == 2
    assert word_ladder("hot", "dog", ["hot", "dog"]) == 0
    assert word_ladder("hot", "hot", ["hot"]) == 1


def _t_14_network_delay_time():
    assert network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert network_delay_time([[1, 2, 1]], 2, 1) == 1
    assert network_delay_time([[1, 2, 1]], 2, 2) == -1
    assert network_delay_time([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1) == 3
    assert network_delay_time([], 1, 1) == 0


def _t_15_cheapest_flights_k_stops():
    f = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert cheapest_flights_k_stops(4, f, 0, 3, 1) == 700
    f = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert cheapest_flights_k_stops(3, f, 0, 2, 1) == 200
    assert cheapest_flights_k_stops(3, f, 0, 2, 0) == 500
    assert cheapest_flights_k_stops(3, [[0, 1, 5]], 0, 2, 1) == -1
    assert cheapest_flights_k_stops(2, [[0, 1, 5]], 0, 0, 0) == 0


def _t_16_min_cost_connect_points():
    assert min_cost_connect_points([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert min_cost_connect_points([[3, 12], [-2, 5], [-4, 1]]) == 18
    assert min_cost_connect_points([[0, 0]]) == 0
    assert min_cost_connect_points([[0, 0], [1, 1], [1, 0], [-1, 1]]) == 4
    assert min_cost_connect_points([[2, -3], [-17, -8], [13, 8], [-17, -15]]) == 53


def _is_alien_order(order, words):
    letters = {c for w in words for c in w}
    if sorted(order) != sorted(letters):
        return False
    pos = {c: i for i, c in enumerate(order)}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if pos[x] >= pos[y]:
                    return False
                break
        else:
            if len(a) > len(b):
                return False
    return True


def _t_17_alien_dictionary():
    w = ["wrt", "wrf", "er", "ett", "rftt"]
    got = alien_dictionary(w)
    assert got == "wertf", got
    assert alien_dictionary(["z", "x"]) == "zx"
    assert alien_dictionary(["z", "x", "z"]) == ""
    assert alien_dictionary(["abc", "ab"]) == ""
    w = ["ac", "ab", "zc", "zb"]
    got = alien_dictionary(w)
    assert _is_alien_order(got, w), got
    got = alien_dictionary(["a", "b", "ca", "cc"])
    assert _is_alien_order(got, ["a", "b", "ca", "cc"]), got


def _t_18_union_find():
    uf = UnionFind(5)
    assert uf.connected(0, 1) is False
    assert uf.union(0, 1) is True
    assert uf.union(1, 2) is True
    assert uf.union(0, 2) is False
    assert uf.connected(0, 2) is True
    assert uf.connected(0, 3) is False
    assert uf.union(3, 4) is True
    assert uf.find(3) == uf.find(4)
    assert uf.find(0) != uf.find(3)
    assert uf.union(4, 0) is True
    assert all(uf.connected(0, i) for i in range(5))


def _check():
    checks = [(n[3:], f) for n, f in sorted(globals().items()) if n.startswith("_t_")]
    passed = 0
    for name, fn in checks:
        try:
            fn()
            print(f"PASS  {name}")
            passed += 1
        except NotImplementedError:
            print(f"TODO  {name}")
        except AssertionError as e:
            print(f"FAIL  {name}  {e}")
        except Exception as e:  # noqa: BLE001 — show the student what blew up
            print(f"FAIL  {name}  {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(checks)} passed")


if __name__ == "__main__":
    _check()
