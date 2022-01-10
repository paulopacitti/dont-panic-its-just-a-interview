# description: https://leetcode.com/problems/merge-intervals/
# tags: amazon greedy

def merge(intervals):
    merged_intervals = []
    current = []
    i = 0
    intervals.sort()
    while i < len(intervals):
        if len(current) == 0:
            current = intervals[i].copy()
            i += 1
        else:
            if (intervals[i][0] >= current[0] and intervals[i][0] <= current[1]) \
                    or (intervals[i][1] >= current[0] and intervals[i][1] <= current[1]):
                if current[0] > intervals[i][0]:
                    current[0] = intervals[i][0]
                if current[1] < intervals[i][1]:
                    current[1] = intervals[i][1]
                i += 1
            else:
                merged_intervals.append(current)
                current = []
    if len(current) != 0:
        merged_intervals.append(current)
    return merged_intervals

a = [[1,4],[4,5]]
print(merge(a))

# Time Complexity: O(nlog n + n), to sort the intervals
# Space Complexity: O(n), to store all the intervals in case these don't overlap