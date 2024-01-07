# description: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []

    queue = []
    level = []
    path = []
    queue.append(root)
    while queue:
        level = []
        current_len = len(queue)
        for i in range(current_len):
            node = queue.pop(0)
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            path.append(level)
            
    return path
