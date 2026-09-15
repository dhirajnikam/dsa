def two_sum_sorted(numbers, target):
    # O(n) time, O(1) space
    # Sorted input: a too-small sum can only be fixed by moving l right, too-big by moving r left.
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        if s < target:
            l += 1
        else:
            r -= 1
    return []
