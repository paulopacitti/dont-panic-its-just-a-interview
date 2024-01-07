# description: https://leetcode.com/problems/search-in-a-binary-search-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(self, root, val):
    if not root:
        return None
    if root.val == val:
        return root
    
    left = self.searchBST(root.left, val)
    right = self.searchBST(root.right, val)
    found = left if left else right
    
    return found   