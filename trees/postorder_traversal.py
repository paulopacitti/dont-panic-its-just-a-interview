# description: https://leetcode.com/problems/binary-tree-postorder-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def postorderTraversal(self, root):
    if not root:
        return []
    
    left = self.postorderTraversal(root.left)
    right = self.postorderTraversal(root.right)
    return left + right + [root.val]