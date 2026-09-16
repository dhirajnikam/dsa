"""11 · Greedy & Intervals — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""
from collections import Counter


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    out: list[list[int]] = []
    for start, end in sorted(intervals, key=lambda iv: iv[0]):
        if out and start <= out[-1][1]:            # overlaps the last kept interval
            out[-1][1] = max(out[-1][1], end)      # max: [1,10],[2,3] stays [1,10]
        else:
            out.append([start, end])
    return out
    # O(n log n) time for the sort, O(n) space for the output.


def insert_interval(intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    i, n = 0, len(intervals)
    while i < n and intervals[i][1] < new[0]:      # entirely before new
        out.append(intervals[i])
        i += 1
    lo, hi = new
    while i < n and intervals[i][0] <= hi:         # overlapping: absorb into new
        lo = min(lo, intervals[i][0])
        hi = max(hi, intervals[i][1])
        i += 1
    out.append([lo, hi])
    out.extend(intervals[i:])                      # entirely after
    return out
    # O(n) time, no sort needed because the input is sorted.


def non_overlapping_intervals(intervals: list[list[int]]) -> int:
    kept, last_end = 0, float("-inf")
    for start, end in sorted(intervals, key=lambda iv: iv[1]):   # by END
        if start >= last_end:                      # touching is fine here
            kept += 1
            last_end = end
    return len(intervals) - kept
    # Activity selection. O(n log n).


def can_attend_meetings(intervals: list[list[int]]) -> bool:
    ivs = sorted(intervals, key=lambda iv: iv[0])
    for prev, cur in zip(ivs, ivs[1:]):
        if cur[0] < prev[1]:                       # starts before the previous one ends
            return False
    return True
    # O(n log n).


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    events: list[tuple[int, int]] = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort()                                  # (t, -1) before (t, +1): free a room first
    rooms = best = 0
    for _, delta in events:
        rooms += delta
        best = max(best, rooms)
    return best
    # Sweep line. O(n log n) time, O(n) space.


def jump_game(nums: list[int]) -> bool:
    reach = 0                                      # farthest index reachable so far
    for i, x in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True
    # O(n) time, O(1) space.


def jump_game_ii(nums: list[int]) -> int:
    jumps = cur_end = farthest = 0
    for i in range(len(nums) - 1):                 # never jump from the last index
        farthest = max(farthest, i + nums[i])
        if i == cur_end:                           # edge of the current BFS level
            jumps += 1
            cur_end = farthest
    return jumps
    # O(n) time, O(1) space. BFS by levels without a queue.


def gas_station(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1                                  # not enough gas overall
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:                               # no station in [start, i] can be the start
            start, tank = i + 1, 0
    return start
    # O(n) time, O(1) space.


def hand_of_straights(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size:
        return False
    counts = Counter(hand)
    for card in sorted(counts):                    # smallest remaining card must start a group
        need = counts[card]
        if need == 0:
            continue
        for v in range(card, card + group_size):
            if counts[v] < need:
                return False
            counts[v] -= need
    return True
    # O(n log n) for the sort; each card is decremented once.


def partition_labels(s: str) -> list[int]:
    last = {c: i for i, c in enumerate(s)}         # last index of each letter
    out: list[int] = []
    start = end = 0
    for i, c in enumerate(s):
        end = max(end, last[c])                    # the part must reach c's last occurrence
        if i == end:                               # nothing seen so far appears later
            out.append(end - start + 1)
            start = i + 1
    return out
    # O(n) time, O(1) space (26 letters).


def valid_parenthesis_string(s: str) -> bool:
    lo = hi = 0                                    # min and max possible unmatched '('
    for c in s:
        if c == "(":
            lo += 1
            hi += 1
        elif c == ")":
            lo -= 1
            hi -= 1
        else:                                      # '*': ')' lowers, '(' raises, '' keeps
            lo -= 1
            hi += 1
        if hi < 0:
            return False                           # too many ')' even if every '*' is '('
        lo = max(lo, 0)                            # cannot have fewer than 0 open
    return lo == 0
    # O(n) time, O(1) space.


def min_arrows_burst_balloons(points: list[list[int]]) -> int:
    arrows, last_arrow = 0, float("-inf")
    for start, end in sorted(points, key=lambda p: p[1]):   # by END
        if start > last_arrow:                     # this balloon is not burst yet
            arrows += 1
            last_arrow = end                       # shoot at the earliest end
    return arrows
    # O(n log n). Touching balloons share an arrow, hence '>' not '>='.


def assign_cookies(greed: list[int], sizes: list[int]) -> int:
    greed.sort()
    sizes.sort()
    i = 0                                          # next child to satisfy
    for cookie in sizes:                           # smallest cookie first
        if i < len(greed) and cookie >= greed[i]:
            i += 1
    return i
    # O(n log n + m log m).


def two_city_scheduling(costs: list[list[int]]) -> int:
    ordered = sorted(costs, key=lambda c: c[0] - c[1])   # most "prefers A" first
    n = len(costs) // 2
    return sum(c[0] for c in ordered[:n]) + sum(c[1] for c in ordered[n:])
    # O(n log n). Sorting by the difference is the exchange argument in code.


def interval_intersections(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    out: list[list[int]] = []
    i = j = 0
    while i < len(a) and j < len(b):
        lo = max(a[i][0], b[j][0])
        hi = min(a[i][1], b[j][1])
        if lo <= hi:
            out.append([lo, hi])
        if a[i][1] < b[j][1]:                      # the one ending first cannot intersect more
            i += 1
        else:
            j += 1
    return out
    # O(n + m) time.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
