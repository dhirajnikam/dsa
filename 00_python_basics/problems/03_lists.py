"""
Problem: List basics
Difficulty: Warm-up | Topic: indexing, iteration, in-place vs copy

1. second_largest([3, 1, 4, 4, 2]) -> 3   (distinct values; return None if fewer than 2 distinct)
2. running_sum([1, 2, 3, 4]) -> [1, 3, 6, 10]   (LeetCode 1480)
3. rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]   k may exceed len; return a new list
4. remove_duplicates_keep_order([1, 3, 1, 2, 3]) -> [1, 3, 2]

Hints:
1. sorted(set(nums)) gives distinct values in order.
3. k %= len(nums); then slice.
4. A set tracks what you have seen; a list keeps order.
"""


def second_largest(nums: list[int]):
    largest = nums[0]
    list_sec = []
    for n in nums:
        if largest < n: 
            largest = n
    for n in nums:
        if n != largest:
            list_sec.append(n)
    if list_sec != []:
        largest = list_sec[0]
        for n in list_sec:
            if largest < n: 
                largest = n
        return largest
    else:
        return None 




def running_sum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
           


def rotate_right(nums: list[int], k: int) -> list[int]:
    if not nums:
        return []
    k %= len(nums)
    list_rotate = nums[-k:]
    return  list_rotate + nums[:-k] 


def remove_duplicates_keep_order(nums: list[int]) -> list[int]:
    seen = set()
    order = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            order.append(num)
    return order 

    


if __name__ == "__main__":
    assert second_largest([3, 1, 4, 4, 2]) == 3
    assert second_largest([5, 5]) is None
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([]) == []
    assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_right([1, 2, 3], 4) == [3, 1, 2]
    assert rotate_right([], 3) == []
    assert remove_duplicates_keep_order([1, 3, 1, 2, 3]) == [1, 3, 2]
    print("ok")
