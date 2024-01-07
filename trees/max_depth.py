# description: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root):
    if not root:
        return 0
    
    left = 1 + self.maxDepth(root.left)
    right = 1 + self.maxDepth(root.right)
    return max(left, right)