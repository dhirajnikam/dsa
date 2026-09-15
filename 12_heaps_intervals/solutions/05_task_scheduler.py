import heapq
from collections import Counter, deque


def least_interval(tasks, n):
    # O(T) time, O(1) space (at most 26 distinct tasks in heap/queue)
    # Each tick, run the most frequent available task (max-heap); it then waits in a
    # cooldown deque until time + n, when it goes back to the heap.
    heap = [-c for c in Counter(tasks).values()]
    heapq.heapify(heap)
    cooling = deque()  # (ready_time, negative remaining count)
    t = 0
    while heap or cooling:
        t += 1
        if heap:
            cnt = heapq.heappop(heap) + 1  # one less remaining (counts are negative)
            if cnt:
                cooling.append((t + n, cnt))
        if cooling and cooling[0][0] == t:
            heapq.heappush(heap, cooling.popleft()[1])
    return t
