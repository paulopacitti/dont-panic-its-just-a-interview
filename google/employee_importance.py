# description: https://leetcode.com/problems/employee-importance/
# tags: bfs
# Solution: Breadth First Search


def getImportance(employees, id):
    total_importance = 0
    stack = [id]  # Breadth First Search stack
    table = {}

    for e in employees:  # create table for O(1) access to employee, given id
        table[e.id] = e

    while stack:
        e = table[stack.pop()]
        total_importance += e.importance
        if e.subordinates:
            stack.extend(e.subordinates)  # add subordinates to the stack

    return total_importance


# Time complexity: O(n), size of the stack, where all the employees are subordinates of one boss
# Space complexity: O(n), where n is the number of employees
