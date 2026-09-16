"""
Problem: Cheapest Flights Within K Stops
Difficulty: Medium | Pattern: Bellman-Ford with bounded rounds
Source: LeetCode 787

There are n cities and flights[i] = [from, to, price]. Return the cheapest price from src
to dst with at most k stops (so at most k+1 flights), or -1 if there is no such route.

Example 1:
  n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1 -> 700
Example 2:
  n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1 -> 200
Example 3:
  n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0 -> 500

Constraints:
  1 <= n <= 100
  0 <= k < n
  No duplicate flights.

Hints:
1. Plain Dijkstra fails: the cheapest path may use too many edges. You need edge count as state.
2. Bellman-Ford: run k+1 relaxation rounds. Relax from a COPY of the previous round's
   distances so each round adds at most one flight.
3. Alternative: BFS by layers (stops) or Dijkstra on (cost, node, stops_used).

Expected: O(k * E) time, O(V) space
"""


def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    f = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert find_cheapest_price(4, f, 0, 3, 1) == 700, 'Check: find_cheapest_price(4, f, 0, 3, 1) == 700'
    f = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert find_cheapest_price(3, f, 0, 2, 1) == 200, 'Check: find_cheapest_price(3, f, 0, 2, 1) == 200'
    assert find_cheapest_price(3, f, 0, 2, 0) == 500, 'Check: find_cheapest_price(3, f, 0, 2, 0) == 500'
    assert find_cheapest_price(3, f, 2, 0, 2) == -1, 'Check: find_cheapest_price(3, f, 2, 0, 2) == -1'
    assert find_cheapest_price(1, [], 0, 0, 0) == 0, 'Check: find_cheapest_price(1, [], 0, 0, 0) == 0'
    assert find_cheapest_price(2, [[0, 1, 5]], 0, 1, 0) == 5, 'Check: find_cheapest_price(2, [[0, 1, 5]], 0, 1, 0) == 5'
    f = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]]
    assert find_cheapest_price(4, f, 0, 3, 2) == 3, 'Check: find_cheapest_price(4, f, 0, 3, 2) == 3'
    assert find_cheapest_price(4, f, 0, 3, 1) == 10, 'Check: find_cheapest_price(4, f, 0, 3, 1) == 10'
    f = [[0, 1, 2], [1, 2, 1], [2, 0, 10], [1, 3, 4], [2, 3, 1]]
    assert find_cheapest_price(4, f, 0, 3, 2) == 4, 'Check: find_cheapest_price(4, f, 0, 3, 2) == 4'
    print("ok")
