# description: https://leetcode.com/problems/asteroid-collision


def collide(asteroids):
    if len(asteroids) < 2:  # only one asteroid detected. no collision
        return
    if (asteroids[-1] > 0 and asteroids[-2] > 0) or (
        asteroids[-1] < 0 and asteroids[-2] < 0
    ):  # check if top 2 asteroids have the same direction
        return
    else:
        right = asteroids.pop()
        left = asteroids.pop()
        if left < 0:  # check if the top element has right-to-left direction
            asteroids.append(left)
            asteroids.append(right)
            return
        if abs(right) == abs(left):  # both asteroids explode
            collide(asteroids)
        elif abs(right) > abs(left):
            asteroids.append(right)
            collide(asteroids)
        elif abs(left) > abs(right):
            asteroids.append(left)
            collide(asteroids)


def asteroidCollision(asteroids):
    stack = []

    for a in asteroids:
        stack.append(a)
        if a < 0:  # possible colision detected
            collide(stack)

    return stack


asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))

# Time complexity: O(N), where N is the number of asteroids
# Space complexity: O(N), to store the N elements in the stack
