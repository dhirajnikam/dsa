def find_cheapest_price(n, flights, src, dst, k):
    # O(k * E) time, O(V) space
    # Bellman-Ford limited to k+1 rounds; relaxing from a snapshot of the previous round
    # guarantees round i only uses paths with at most i flights.
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        prev = dist[:]
        for u, v, w in flights:
            if prev[u] + w < dist[v]:
                dist[v] = prev[u] + w
    return dist[dst] if dist[dst] < INF else -1
