# description: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(self, root):
    if not root:
        return 0

    left = 1 + self.minDepth(root.left)
    right = 1 + self.minDepth(root.right)

    if left == 1: # it means left is a null subtree
        return right
    elif right == 1: # it means right is a null subtree
        return left
    else:
        return min(left, right)