# description: https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
#     1
#    / \
#   2   3
#  /\   /\ 
# 7  6  5 4

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = None

def diameter(root):
    if root != None:
        height, diameter = diameter_util(root, 1)
        return diameter
    else:
        return 0

def diameter_util(root, diameter):
    if root == None:
        return 0, diameter
    left_height, diameter = diameter_util(root.left, diameter)
    right_height, diameter = diameter_util(root.right, diameter)
    
    height = 1 + max(left_height, right_height)
    diameter = max(diameter, 1 + left_height + right_height)

    return height, diameter


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print(diameter(root))

# Time complexity: O(n), where n is the number of nodes
# Space complexity: O(1), no extra space required