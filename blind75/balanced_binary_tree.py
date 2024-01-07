class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
        balanced, tall = height(root)
        return balanced

def height(root):
    if root == None:
        return (True, 0)
    left_balanced, left_height = height(root.left)
    right_balanced, right_height = height(root.right)

    balanced = left_balanced and right_balanced and (abs(left_height-right_height) <= 1)
    tall = max(left_height, right_height) + 1

    return (balanced, tall)