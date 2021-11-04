# description: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    queue = []
    queue.append(root)
    level = 0
    while len(queue) > 0:
        node_count = len(queue) # number of nodes in level
        while node_count > 0: # when it's negative, it increased level
            current = queue.pop(0)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
            node_count -= 1
        level += 1
    return level-1
     

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))

# Time complexity: O(n), where n is the number of nodes
# Space complexity: O(w), where w is the max width of the tree.
