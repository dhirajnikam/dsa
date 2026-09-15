from collections import deque


def sliding_window_max_naive(nums, k):  # O(n*k) time, O(k) space
    if k == 0 or k > len(nums):
        return []
    window = deque(nums[:k])
    out = [max(window)]
    for i in range(k, len(nums)):
        window.popleft()
        window.append(nums[i])
        out.append(max(window))
    return out


def rotate(nums, k):  # O(n)
    dq = deque(nums)
    dq.rotate(k)
    return list(dq)


def tail(lines, n):  # O(len(lines)) time, O(n) space
    if n == 0:
        return []
    return list(deque(lines, maxlen=n))


def is_palindrome_deque(s):  # O(n)
    dq = deque(ch.lower() for ch in s if ch.isalnum())
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


def hot_potato(names, num):  # O(n * num)
    dq = deque(names)
    while len(dq) > 1:
        dq.rotate(-num)
        dq.popleft()
    return dq[0]
