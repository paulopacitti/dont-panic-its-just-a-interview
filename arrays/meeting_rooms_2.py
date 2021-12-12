# description: https://www.lintcode.com/problem/919/

# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: 2
# Explanation:
# We need two meeting rooms
# room1: (0,30)
# room2: (5,10),(15,20)
import heapq

def meeting_rooms_2_heap(intervals):
    intervals.sort()
    ending_times_heap = []
    rooms = 0
    
    for meeting in intervals:
        heapq.heappush(ending_times_heap, meeting[1])
        if meeting[0] < ending_times_heap[0]:
            rooms += 1
        else:
             heapq.heappop(ending_times_heap)

    return rooms

# Time Complexity: O(n log n)
# Space Complexity: O(n)

def meeting_rooms_2(intervals):
    starting_times = []
    ending_times = []
    current_meetings = 0
    max_rooms = 0
    for e in intervals:
        starting_times.append(e[0])
        ending_times.append(e[1])
    
    starting_times.sort()
    ending_times.sort()
    
    i = 0
    j = 0
    while i < len(intervals) and j < len(intervals):
        if starting_times[i] < ending_times[j]:
            i += 1
            current_meetings += 1
        else:
            j += 1
            current_meetings -= 1
        max_rooms = max(max_rooms, current_meetings)
    return max_rooms

# Time Complexity: O(n log n)
# Space Complexity: O(n)

a = [[0, 30],[5, 10],[15, 20]]
print(meeting_rooms_2(a))