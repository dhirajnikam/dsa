"""11 · Greedy & Intervals — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
For every greedy choice, say the exchange argument out loud before you trust it.
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge all overlapping closed intervals and return them sorted by start.
    Touching intervals ([1,4] and [4,5]) merge.
    [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]] ; [[1,4],[4,5]] -> [[1,5]]
    """
    raise NotImplementedError


def insert_interval(intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    """intervals is sorted by start and pairwise disjoint. Insert new, merging as needed,
    and return the result still sorted and disjoint.
    [[1,3],[6,9]], [2,5] -> [[1,5],[6,9]]
    [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8] -> [[1,2],[3,10],[12,16]]
    """
    raise NotImplementedError


def non_overlapping_intervals(intervals: list[list[int]]) -> int:
    """Minimum number of intervals to remove so the rest do not overlap.
    Touching intervals ([1,2] and [2,3]) do NOT overlap.
    [[1,2],[2,3],[3,4],[1,3]] -> 1 ; [[1,2],[1,2],[1,2]] -> 2 ; [[1,2],[2,3]] -> 0
    """
    raise NotImplementedError


def can_attend_meetings(intervals: list[list[int]]) -> bool:
    """True if no two meetings overlap. A meeting ending at t and one starting at t are fine.
    [[0,30],[5,10],[15,20]] -> False ; [[7,10],[2,4]] -> True ; [[1,5],[5,10]] -> True
    """
    raise NotImplementedError


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """Minimum rooms so that every meeting has a room. A room freed at t can be reused at t.
    Use the sweep line here (the heap version lives in Chapter 07).
    [[0,30],[5,10],[15,20]] -> 2 ; [[7,10],[2,4]] -> 1 ; [[1,5],[5,10]] -> 1
    """
    raise NotImplementedError


def jump_game(nums: list[int]) -> bool:
    """You start at index 0; nums[i] is the farthest you may jump from i. Can you reach the
    last index?
    [2,3,1,1,4] -> True ; [3,2,1,0,4] -> False ; [0] -> True
    """
    raise NotImplementedError


def jump_game_ii(nums: list[int]) -> int:
    """Same rules as jump_game; the last index is always reachable. Return the minimum
    number of jumps.
    [2,3,1,1,4] -> 2 ; [2,3,0,1,4] -> 2 ; [0] -> 0
    """
    raise NotImplementedError


def gas_station(gas: list[int], cost: list[int]) -> int:
    """Circular route. Station i gives gas[i]; driving from i to i+1 costs cost[i]. Starting
    with an empty tank, return the unique start index that completes the loop, or -1.
    [1,2,3,4,5], [3,4,5,1,2] -> 3 ; [2,3,4], [3,4,3] -> -1 ; [5], [4] -> 0
    """
    raise NotImplementedError


def hand_of_straights(hand: list[int], group_size: int) -> bool:
    """Can the cards be split into groups of exactly group_size consecutive values?
    [1,2,3,6,2,3,4,7,8], 3 -> True ([1,2,3],[2,3,4],[6,7,8]) ; [1,2,3,4,5], 4 -> False
    [8,10,12], 1 -> True
    """
    raise NotImplementedError


def partition_labels(s: str) -> list[int]:
    """Cut s into as many parts as possible so that every letter appears in at most one
    part. Return the part sizes in order.
    "ababcbacadefegdehijhklij" -> [9, 7, 8] ; "eccbbbbdec" -> [10] ; "abc" -> [1, 1, 1]
    """
    raise NotImplementedError


def valid_parenthesis_string(s: str) -> bool:
    """s contains '(', ')', and '*'. Each '*' may act as '(', ')', or nothing. True if some
    choice makes s a valid parenthesis string.
    "()" -> True ; "(*)" -> True ; "(*))" -> True ; "((*" -> False
    """
    raise NotImplementedError


def min_arrows_burst_balloons(points: list[list[int]]) -> int:
    """Each balloon spans [x_start, x_end] horizontally. A vertical arrow shot at x bursts
    every balloon with x_start <= x <= x_end. Return the minimum number of arrows.
    [[10,16],[2,8],[1,6],[7,12]] -> 2 ; [[1,2],[3,4],[5,6],[7,8]] -> 4 ; [[1,2],[2,3],[3,4],[4,5]] -> 2
    """
    raise NotImplementedError


def assign_cookies(greed: list[int], sizes: list[int]) -> int:
    """Child i is content with a cookie of size >= greed[i]. Each child gets at most one
    cookie. Return the maximum number of content children.
    [1,2,3], [1,1] -> 1 ; [1,2], [1,2,3] -> 2 ; [], [1] -> 0
    """
    raise NotImplementedError


def two_city_scheduling(costs: list[list[int]]) -> int:
    """costs[i] = [a, b]: flying person i to city A costs a, to city B costs b. Exactly half
    of the 2n people must go to each city. Return the minimum total cost.
    [[10,20],[30,200],[400,50],[30,20]] -> 110 ; [[1,2],[2,1]] -> 2
    """
    raise NotImplementedError


def interval_intersections(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """a and b are each sorted lists of pairwise-disjoint closed intervals. Return every
    intersection, sorted.
    [[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]
        -> [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    [[1,3]], [[4,5]] -> []
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_merge_intervals():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([]) == []
    assert merge_intervals([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]


def _t_02_insert_interval():
    assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert insert_interval([], [5, 7]) == [[5, 7]]
    assert insert_interval([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert insert_interval([[3, 5]], [1, 2]) == [[1, 2], [3, 5]]


def _t_03_non_overlapping_intervals():
    assert non_overlapping_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert non_overlapping_intervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert non_overlapping_intervals([[1, 2], [2, 3]]) == 0
    assert non_overlapping_intervals([]) == 0
    assert non_overlapping_intervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2


def _t_04_can_attend_meetings():
    assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) is False
    assert can_attend_meetings([[7, 10], [2, 4]]) is True
    assert can_attend_meetings([]) is True
    assert can_attend_meetings([[1, 5], [5, 10]]) is True


def _t_05_min_meeting_rooms():
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([]) == 0
    assert min_meeting_rooms([[1, 5], [5, 10]]) == 1
    assert min_meeting_rooms([[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]) == 4


def _t_06_jump_game():
    assert jump_game([2, 3, 1, 1, 4]) is True
    assert jump_game([3, 2, 1, 0, 4]) is False
    assert jump_game([0]) is True
    assert jump_game([0, 1]) is False
    assert jump_game([1, 0, 1]) is False


def _t_07_jump_game_ii():
    assert jump_game_ii([2, 3, 1, 1, 4]) == 2
    assert jump_game_ii([2, 3, 0, 1, 4]) == 2
    assert jump_game_ii([0]) == 0
    assert jump_game_ii([1, 2]) == 1
    assert jump_game_ii([1, 1, 1, 1]) == 3


def _t_08_gas_station():
    assert gas_station([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert gas_station([2, 3, 4], [3, 4, 3]) == -1
    assert gas_station([5], [4]) == 0
    assert gas_station([3, 1, 1], [1, 2, 2]) == 0
    assert gas_station([1, 2], [2, 1]) == 1


def _t_09_hand_of_straights():
    assert hand_of_straights([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
    assert hand_of_straights([1, 2, 3, 4, 5], 4) is False
    assert hand_of_straights([8, 10, 12], 1) is True
    assert hand_of_straights([1, 1, 2, 2, 3, 3], 3) is True
    assert hand_of_straights([1, 2, 3, 4], 2) is True
    assert hand_of_straights([1, 1, 3, 3], 2) is False


def _t_10_partition_labels():
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert partition_labels("eccbbbbdec") == [10]
    assert partition_labels("abc") == [1, 1, 1]
    assert partition_labels("a") == [1]


def _t_11_valid_parenthesis_string():
    assert valid_parenthesis_string("()") is True
    assert valid_parenthesis_string("(*)") is True
    assert valid_parenthesis_string("(*))") is True
    assert valid_parenthesis_string("((*") is False
    assert valid_parenthesis_string(")(") is False
    assert valid_parenthesis_string("") is True
    assert valid_parenthesis_string("*") is True
    assert valid_parenthesis_string("(**") is True


def _t_12_min_arrows_burst_balloons():
    assert min_arrows_burst_balloons([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert min_arrows_burst_balloons([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert min_arrows_burst_balloons([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert min_arrows_burst_balloons([]) == 0
    assert min_arrows_burst_balloons([[1, 10]]) == 1


def _t_13_assign_cookies():
    assert assign_cookies([1, 2, 3], [1, 1]) == 1
    assert assign_cookies([1, 2], [1, 2, 3]) == 2
    assert assign_cookies([], [1]) == 0
    assert assign_cookies([1], []) == 0
    assert assign_cookies([10, 9, 8, 7], [5, 6, 7, 8]) == 2


def _t_14_two_city_scheduling():
    assert two_city_scheduling([[10, 20], [30, 200], [400, 50], [30, 20]]) == 110
    assert two_city_scheduling([[1, 2], [2, 1]]) == 2
    assert two_city_scheduling([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]) == 1859
    assert two_city_scheduling([[515, 563], [451, 713], [537, 709], [343, 819],
                                [855, 779], [457, 60], [650, 359], [631, 42]]) == 3086


def _t_15_interval_intersections():
    a = [[0, 2], [5, 10], [13, 23], [24, 25]]
    b = [[1, 5], [8, 12], [15, 24], [25, 26]]
    assert interval_intersections(a, b) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert interval_intersections([], [[1, 2]]) == []
    assert interval_intersections([[1, 3]], [[4, 5]]) == []
    assert interval_intersections([[1, 5]], [[2, 3]]) == [[2, 3]]
    assert interval_intersections([[1, 7]], [[3, 10]]) == [[3, 7]]


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
