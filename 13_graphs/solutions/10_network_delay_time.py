import heapq
from collections import defaultdict


def network_delay_time(times, n, k):
    # O((V + E) log V) time, O(V + E) space
    # Dijkstra from k with lazy deletion; the answer is the largest finalized distance.
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    dist = {}
    heap = [(0, k)]
    while heap:
        d, u = heapq.heappop(heap)
        if u in dist:
            continue
        dist[u] = d
        for v, w in graph[u]:
            if v not in dist:
                heapq.heappush(heap, (d + w, v))
    return max(dist.values()) if len(dist) == n else -1
