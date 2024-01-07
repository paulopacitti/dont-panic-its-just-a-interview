# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right        

def preorderTraversal(self, root):
    if not root:
            return []
        
    left = self.preorderTraversal(root.left)
    right = self.preorderTraversal(root.right)
    return [root.val] + left + right    
    