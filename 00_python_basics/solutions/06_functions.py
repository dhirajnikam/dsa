def min_max(nums):
    lo = hi = nums[0]
    for x in nums[1:]:
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return lo, hi


def append_safe(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


def apply_n(f, x, n):
    for _ in range(n):
        x = f(x)
    return x


def swap_in_place(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
