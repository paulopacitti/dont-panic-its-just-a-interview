# description: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    if not root:
        return []
    
    left = inorderTraversal(root.left)
    right = inorderTraversal(root.right)
    path = left + [root.val] + right
    
    return path

node_3 = TreeNode(3)
node_2 = TreeNode(val=2, left=node_3)
root = TreeNode(1, right=node_2)

print(inorderTraversal(root))