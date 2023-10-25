# description: https://leetcode.com/problems/balanced-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    return height(root)[0]


def height(node):
    if node == None:
        return (True, 0)
    else:
        left = height(node.left)
        right = height(node.right)

        difference = abs(left[1] - right[1])
        balanced = left[0] and right[0] and difference <= 1
        depth = 1 + max(left[1], right[1])

        return (balanced, depth)


# Time complexity: O(n)
# Space complexity: O(n)
