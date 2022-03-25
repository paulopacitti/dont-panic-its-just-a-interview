# description: https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-sumtree/
class Node:
    def __init__(self, x):
       
        self.data = x
        self.left = None
        self.right = None

def sum_tree(root):
    if root == None:
        return 0
    else:
        left = sum_tree(root.left)
        if left == -1:
            return -1
        
        right = sum_tree(root.right)
        if right == -1:
            return -1

        if left + right == root.data or (root.left == None and root.right == None):
            return left + right + root.data
        else:
            return -1

def is_sum_tree(root):
    if sum_tree(root) > 0:
        return True
    else:
        return False

root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)

if(is_sum_tree(root)):
    print("The given tree is a SumTree ")
else:
    print("The given tree is not a SumTree ")

# Time complexity: O(n)
# Space complexity: O(n)