# description: https://leetcode.com/problems/maximum-units-on-a-truck

import heapq

def maximum_units(boxTypes, truckSize):
    boxTypes.sort(key = lambda k: k[1], reverse = True)
    truck = 0
    units = 0
    full = False
    while not full and len(boxTypes) != 0:
        current_box_type = boxTypes.pop(0)
        for j in range(current_box_type[0]):
            if truck + 1 > truckSize:
                full = True
                break
            else:
                truck += 1
                units += current_box_type[1]
    
    return units

def maximum_units_heap(boxTypes, truckSize):
    for i in range(len(boxTypes)):
        boxTypes[i][0], boxTypes[i][1] = -boxTypes[i][1], boxTypes[i][0]
    heapq.heapify(boxTypes)
    truck = 0
    units = 0
    full = False
    while not full and len(boxTypes) != 0:
        current_box_type = heapq.heappop(boxTypes)
        for j in range(current_box_type[1]):
            if truck + 1 > truckSize:
                full = True
                break
            else:
                truck += 1
                units += -current_box_type[0]
    
    return units

warehouse = [[1,3],[2,2],[3,1]]
print(maximum_units(warehouse, 4))

# Time complexity: O(n log (n))
# Space complexity: O(1)
