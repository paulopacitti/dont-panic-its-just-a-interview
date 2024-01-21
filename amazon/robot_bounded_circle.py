# description: https://leetcode.com/problems/robot-bounded-in-circle
# tags: amazon greedy

def is_robot_bounded(instructions):
    directions = ["N", "E", "S", "W"]
    coordinates = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    current_direction = 0
    current_position = (0, 0)

    for inst in instructions:
        if inst == "R":
            current_direction = (current_direction + 1) % len(directions)
        elif inst == "L":
            current_direction = (current_direction - 1) % len(directions)
        elif inst == "G":
            current_position = (current_position[0] + coordinates[current_direction][0], current_position[1] + coordinates[current_direction][1])
    
    print(current_direction, current_position)
    return current_direction != 0 or current_position == (0,0)

print(is_robot_bounded('GGLLGG'))

# Time complexity: O(L), where L is the number of robot commands
# Space complexity: O(1)