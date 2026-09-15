from collections import deque


def can_finish(num_courses, prerequisites):
    # O(V + E) time, O(V + E) space
    # Kahn's algorithm: peel off in-degree-0 nodes; if every node gets peeled there is no cycle.
    graph = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        graph[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    taken = 0
    while q:
        node = q.popleft()
        taken += 1
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return taken == num_courses
