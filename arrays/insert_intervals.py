# description: https://leetcode.com/problems/insert-interval/description/

def insert(intervals, newInterval):
    new_list = []
    
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]: # no more overlapping intervals
            new_list.append(newInterval)
            return new_list + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            new_list.append(intervals[i])
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]
    new_list.append(newInterval)
    
    return new_list

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print(insert(intervals, newInterval))
        