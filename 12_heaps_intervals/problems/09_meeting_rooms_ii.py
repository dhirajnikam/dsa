"""
Problem: Meeting Rooms II
Difficulty: Medium | Pattern: min-heap of end times / sweep line
Source: LeetCode 253

Given an array of meeting time intervals [start, end), return the minimum number of
conference rooms required. A meeting ending at t and another starting at t can share a room.

Example 1:
  intervals = [[0, 30], [5, 10], [15, 20]] -> 2
Example 2:
  intervals = [[7, 10], [2, 4]] -> 1

Constraints:
  1 <= len(intervals) <= 10^4
  0 <= start < end <= 10^6

Hints:
1. Sort by start. A min-heap holds the end times of meetings currently occupying rooms.
2. For each meeting, if heap[0] <= start, that room is free: pop it. Then push this end.
   The heap size is the number of rooms in use; track its maximum.
3. Alternative: sweep line with +1 at starts and -1 at ends; answer = max running sum.

Expected: O(n log n) time, O(n) space
"""
import heapq


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2, 'Check: min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2'
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1, 'Check: min_meeting_rooms([[7, 10], [2, 4]]) == 1'
    assert min_meeting_rooms([[1, 5]]) == 1, 'Check: min_meeting_rooms([[1, 5]]) == 1'
    assert min_meeting_rooms([[1, 5], [5, 10]]) == 1, 'Check: min_meeting_rooms([[1, 5], [5, 10]]) == 1'
    assert min_meeting_rooms([[1, 5], [2, 6], [3, 7], [4, 8]]) == 4, 'Check: min_meeting_rooms([[1, 5], [2, 6], [3, 7], [4, 8]]) == 4'
    assert min_meeting_rooms([[1, 10], [2, 3], [3, 4], [4, 5]]) == 2, 'Check: min_meeting_rooms([[1, 10], [2, 3], [3, 4], [4, 5]]) == 2'
    assert min_meeting_rooms([[13, 15], [1, 13], [6, 9]]) == 2, 'Check: min_meeting_rooms([[13, 15], [1, 13], [6, 9]]) == 2'
    assert min_meeting_rooms([[9, 10], [4, 9], [4, 17]]) == 2, 'Check: min_meeting_rooms([[9, 10], [4, 9], [4, 17]]) == 2'
    print("ok")
