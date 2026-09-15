"""
Problem: deque basics
Difficulty: Easy | Topic: collections.deque, O(1) ends, maxlen, rotate
Source: LeetCode 239 (naive version), 189

1. sliding_window_max_naive(nums, k) -> list of max of every window of size k.
   Keep the current window in a deque; append the new item, popleft the old one, take max().
   O(n*k) is fine here; the O(n) monotonic deque comes in phase 07.
   [1,3,-1,-3,5,3,6,7], k=3 -> [3,3,5,5,6,7]. Return [] if k > len(nums) or k == 0.
2. rotate(nums, k) -> new list rotated right by k (k may exceed len or be negative). Use deque.rotate.
3. tail(lines, n) -> last n items of an iterable, in order, using deque(maxlen=n). Works on
   generators without materializing them. n == 0 -> [].
4. is_palindrome_deque(s) -> compare popleft() and pop() until the deque has < 2 items.
   Consider only alphanumeric characters, case-insensitive.
5. hot_potato(names, num) -> the last name remaining when you repeatedly pass the potato
   num times (rotate left by 1 each pass) and then remove the holder (the front).
   hot_potato(["a","b","c","d"], 2) -> "a"

Hints:
1. from collections import deque; window = deque(nums[:k]); then loop i from k to len(nums).
2. rotate(k) rotates right; negative k rotates left. deque handles k > len correctly.
5. while len(dq) > 1: for _ in range(num): dq.append(dq.popleft()); dq.popleft()
"""
from collections import deque


def sliding_window_max_naive(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError


def rotate(nums: list, k: int) -> list:
    raise NotImplementedError


def tail(lines, n: int) -> list:
    raise NotImplementedError


def is_palindrome_deque(s: str) -> bool:
    raise NotImplementedError


def hot_potato(names: list[str], num: int) -> str:
    raise NotImplementedError


if __name__ == "__main__":
    assert sliding_window_max_naive([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_max_naive([1], 1) == [1]
    assert sliding_window_max_naive([1, 2], 3) == [] and sliding_window_max_naive([1], 0) == []
    assert sliding_window_max_naive([4, 3, 2, 1], 2) == [4, 3, 2]
    assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate([1, 2, 3], 4) == [3, 1, 2] and rotate([1, 2, 3], -1) == [2, 3, 1]
    assert rotate([], 3) == []
    assert tail(range(10), 3) == [7, 8, 9]
    assert tail((x * x for x in range(10**6)), 2) == [(10**6 - 2) ** 2, (10**6 - 1) ** 2]
    assert tail([1, 2], 5) == [1, 2] and tail([1, 2], 0) == []
    assert is_palindrome_deque("A man, a plan, a canal: Panama")
    assert not is_palindrome_deque("race a car") and is_palindrome_deque("") and is_palindrome_deque("x")
    assert hot_potato(["a", "b", "c", "d"], 2) == "a"
    assert hot_potato(["solo"], 7) == "solo"
    assert hot_potato(["a", "b", "c", "d", "e", "f"], 7) == "c"
    print("ok")
