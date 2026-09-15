from collections import defaultdict, deque


def alien_order(words):
    # O(total characters) time, O(1) space (alphabet is 26 letters)
    # Adjacent words give one edge each at their first differing letter; Kahn's algorithm
    # orders the letters, and a short result (cycle) or a prefix violation returns "".
    graph = defaultdict(set)
    indeg = {ch: 0 for w in words for ch in w}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in graph[x]:
                    graph[x].add(y)
                    indeg[y] += 1
                break
        else:
            if len(a) > len(b):
                return ""
    q = deque(ch for ch, d in indeg.items() if d == 0)
    order = []
    while q:
        ch = q.popleft()
        order.append(ch)
        for nxt in graph[ch]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return "".join(order) if len(order) == len(indeg) else ""
