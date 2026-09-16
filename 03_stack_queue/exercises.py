"""03 · Stack & Queue — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
"""


def valid_parentheses(s: str) -> bool:
    """s contains only ()[]{}. True if every opener is closed by the same type in the right order.
    "()[]{}" -> True ; "([)]" -> False ; "{[]}" -> True ; "" -> True ; "(" -> False
    """
    raise NotImplementedError


class MinStack:
    """A stack whose get_min is O(1), alongside O(1) push / pop / top.
    Hint: push (value, min_so_far) pairs, or keep a second stack of running minimums.
    push(-2); push(0); push(-3); get_min() -> -3; pop(); top() -> 0; get_min() -> -2
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def get_min(self) -> int:
        raise NotImplementedError


def eval_rpn(tokens: list[str]) -> int:
    """Evaluate a Reverse Polish (postfix) expression. Operators + - * /. Division truncates
    toward zero. Tokens are valid; no division by zero.
    ["2","1","+","3","*"] -> 9 ; ["4","13","5","/","+"] -> 6 ; ["3","-4","/"] -> 0
    """
    raise NotImplementedError


def daily_temperatures(temps: list[int]) -> list[int]:
    """ans[i] = number of days after i until a strictly warmer day, 0 if none. O(n).
    [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0] ; [30,40,50,60] -> [1,1,1,0]
    """
    raise NotImplementedError


def next_greater_element(nums: list[int]) -> list[int]:
    """ans[i] = the first value to the right of i that is strictly greater than nums[i],
    or -1 if there is none. O(n).
    [2, 1, 2, 4, 3] -> [4, 2, 4, -1, -1] ; [5, 4, 3] -> [-1, -1, -1]
    """
    raise NotImplementedError


class MyQueue:
    """FIFO queue built from two stacks (Python lists using only append / pop / [-1] / len).
    push / pop / peek / empty, each amortized O(1).
    push(1); push(2); peek() -> 1; pop() -> 1; empty() -> False
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError

    def peek(self) -> int:
        raise NotImplementedError

    def empty(self) -> bool:
        raise NotImplementedError


def simplify_path(path: str) -> str:
    """Canonical form of an absolute Unix path: single slashes, no trailing slash, "." is the
    current directory, ".." goes up one (never above root).
    "/home/" -> "/home" ; "/../" -> "/" ; "/home//foo/" -> "/home/foo" ; "/a/./b/../../c/" -> "/c"
    """
    raise NotImplementedError


def decode_string(s: str) -> str:
    """k[encoded] means encoded repeated k times. Brackets nest. Digits appear only as counts.
    "3[a]2[bc]" -> "aaabcbc" ; "3[a2[c]]" -> "accaccacc" ; "2[abc]3[cd]ef" -> "abcabccdcdcdef"
    """
    raise NotImplementedError


def asteroid_collision(asteroids: list[int]) -> list[int]:
    """Each value is a size; sign is direction (+ right, - left), all same speed. When two meet
    the smaller explodes (both if equal). Return the survivors in order.
    [5, 10, -5] -> [5, 10] ; [8, -8] -> [] ; [10, 2, -5] -> [10] ; [-2, -1, 1, 2] -> [-2, -1, 1, 2]
    """
    raise NotImplementedError


def remove_k_digits(num: str, k: int) -> str:
    """Remove exactly k digits from the decimal string num to make the smallest possible number.
    No leading zeros in the answer; return "0" if nothing is left.
    "1432219", 3 -> "1219" ; "10200", 1 -> "200" ; "10", 2 -> "0"
    """
    raise NotImplementedError


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    """Cars at distinct positions drive toward target at their speeds. A car that catches up
    to a slower one cannot pass; they form a fleet and move at the slower speed. Count the
    fleets that arrive at target.
    12, [10,8,0,5,3], [2,4,1,1,3] -> 3 ; 10, [3], [3] -> 1 ; 100, [0,2,4], [4,2,1] -> 1
    """
    raise NotImplementedError


def largest_rectangle_histogram(heights: list[int]) -> int:
    """Bars of width 1 with the given heights. Largest rectangle area fitting inside. O(n).
    [2, 1, 5, 6, 2, 3] -> 10 (the 5 and 6) ; [2, 4] -> 4 ; [1] -> 1
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_valid_parentheses():
    assert valid_parentheses("()[]{}") is True
    assert valid_parentheses("([)]") is False
    assert valid_parentheses("{[]}") is True
    assert valid_parentheses("") is True
    assert valid_parentheses("(") is False
    assert valid_parentheses("]") is False


def _t_02_min_stack():
    ms = MinStack()
    ms.push(-2); ms.push(0); ms.push(-3)
    assert ms.get_min() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.get_min() == -2
    ms.push(-2); ms.push(5)
    assert ms.get_min() == -2
    ms.pop(); ms.pop()
    assert ms.get_min() == -2
    ms.pop(); ms.pop()
    ms.push(7)
    assert ms.top() == 7 and ms.get_min() == 7


def _t_03_eval_rpn():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["3", "-4", "/"]) == 0
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert eval_rpn(["-7"]) == -7


def _t_04_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
    assert daily_temperatures([50]) == [0]
    assert daily_temperatures([5, 5, 5]) == [0, 0, 0]


def _t_05_next_greater_element():
    assert next_greater_element([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert next_greater_element([5, 4, 3]) == [-1, -1, -1]
    assert next_greater_element([1, 3, 2, 4]) == [3, 4, 4, -1]
    assert next_greater_element([]) == []
    assert next_greater_element([2, 2, 3]) == [3, 3, -1]


def _t_06_my_queue():
    q = MyQueue()
    assert q.empty() is True
    q.push(1); q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False
    q.push(3)
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.empty() is True


def _t_07_simplify_path():
    assert simplify_path("/home/") == "/home"
    assert simplify_path("/../") == "/"
    assert simplify_path("/home//foo/") == "/home/foo"
    assert simplify_path("/a/./b/../../c/") == "/c"
    assert simplify_path("/a/../../b/../c//.//") == "/c"
    assert simplify_path("/...") == "/..."


def _t_08_decode_string():
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert decode_string("abc") == "abc"
    assert decode_string("10[a]") == "a" * 10


def _t_09_asteroid_collision():
    assert asteroid_collision([5, 10, -5]) == [5, 10]
    assert asteroid_collision([8, -8]) == []
    assert asteroid_collision([10, 2, -5]) == [10]
    assert asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    assert asteroid_collision([1, -2, -2, -2]) == [-2, -2, -2]


def _t_10_remove_k_digits():
    assert remove_k_digits("1432219", 3) == "1219"
    assert remove_k_digits("10200", 1) == "200"
    assert remove_k_digits("10", 2) == "0"
    assert remove_k_digits("112", 1) == "11"
    assert remove_k_digits("9", 1) == "0"
    assert remove_k_digits("12345", 2) == "123"


def _t_11_car_fleet():
    assert car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert car_fleet(10, [3], [3]) == 1
    assert car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1
    assert car_fleet(10, [6, 8], [3, 2]) == 2
    assert car_fleet(10, [0, 4, 2], [2, 1, 3]) == 1


def _t_12_largest_rectangle_histogram():
    assert largest_rectangle_histogram([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_histogram([2, 4]) == 4
    assert largest_rectangle_histogram([1]) == 1
    assert largest_rectangle_histogram([2, 2, 2]) == 6
    assert largest_rectangle_histogram([5, 4, 3, 2, 1]) == 9
    assert largest_rectangle_histogram([0]) == 0


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
