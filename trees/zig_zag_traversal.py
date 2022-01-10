# description: 

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zigzag(root):
    queue = []
    direction = "right"
    traversal =  str(root.val) + " "
    queue.append(root)
    while len(queue) > 0:
        depth = []
        current_node = queue.pop(0)
        if current_node.left != None:
            queue.append(current_node.left)
            depth.append(str(current_node.left.val))
        if current_node.right != None:
            queue.append(current_node.right)
            depth.append(str(current_node.right.val))
        if len(depth) > 0:
            if direction == "right":
                depth.reverse()
                traversal += " ".join(depth) + " "
                direction = "left"
            else:
                traversal += " ".join(depth) + " "
                direction = "left"
    return traversal

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("Zigzag Order traversal of binary tree is")
print(zigzag(root))

# Time complexity: same as BFS, O(n) where n is the number of nodes
# Space complexity: (n+1)/2 