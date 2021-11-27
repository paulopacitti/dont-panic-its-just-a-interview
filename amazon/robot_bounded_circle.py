# description: https://leetcode.com/problems/robot-bounded-in-circle
# tags: amazon greedy

def is_robot_bounded(instructions):
    x = 0
    y = 0
    current_direction = 'N'
    directions = {'N': (0,1), 'E': (1, 0), 'S': (0, -1), 'W': (-1,0)}
    for c in instructions:
        if c == 'G':
            x += directions[current_direction][0]
            y += directions[current_direction][1]
        elif c == 'R':
            if current_direction == 'N':
                current_direction = 'E'
            elif current_direction == 'E':
                current_direction = 'S'
            elif current_direction == 'S':
                current_direction = 'W'
            elif current_direction == 'W':
                current_direction = 'N'
        elif c == 'L':
            if current_direction == 'N':
                current_direction = 'W'
            elif current_direction == 'W':
                current_direction = 'S'
            elif current_direction == 'S':
                current_direction = 'E'
            elif current_direction == 'E':
                current_direction = 'N'
    return (x == 0 and y == 0) or current_direction != 'N'

print(is_robot_bounded('GGLLGG'))

# Time complexity: O(L), where L is the number of robot commands
# Space complexity: O(1)