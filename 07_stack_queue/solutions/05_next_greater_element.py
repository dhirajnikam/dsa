def next_greater_element(nums1, nums2):
    # O(n + m) time, O(n) space
    # One monotonic-stack pass over nums2 fills value -> next greater; nums1 is then lookups.
    nxt, stack = {}, []
    for x in nums2:
        while stack and stack[-1] < x:
            nxt[stack.pop()] = x
        stack.append(x)
    return [nxt.get(x, -1) for x in nums1]
