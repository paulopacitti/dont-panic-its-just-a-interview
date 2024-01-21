# description: https://www.geeksforgeeks.org/print-the-longest-path-from-root-to-leaf-in-a-binary-tree/
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def longest_path(root):
    if root == None:
        return []

    left_path = longest_path(root.left)
    right_path = longest_path(root.right)

    if len(left_path) > len(right_path):
        left_path.append(root.data)
    else:
        right_path.append(root.data)

    if len(left_path) > len(right_path):
        return left_path
    else:
        return right_path

#      1
#     /  \
#    2    3
#    /\  
#   4  5  
#       \
#        6  

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)

output = longest_path(root)[::-1]
print(output)

# Time complexity: O(n)
# Space complexity: O(n)
 