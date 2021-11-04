# description: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    result = str(root.info) + " "
    queue = []
    queue.append(root)
    while len(queue) > 0:
        depth = []
        current = queue.pop(0)
        children = [current.left, current.right]
        for child in children:
            if child != None:
                queue.append(child)
                depth.append(str(child.info))
        if len(depth) > 0:
            result += " ".join(depth) + " "
    print(result)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)

# Time complexity: O(n), where n is the number o nodes
# Space complexity: O(w), where w is the max width of the tree.
# A balanced tree would have w=n/2 while a n-ary tree could have w=n.
