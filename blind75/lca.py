# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# find the split approach, recursive
def lowestCommonAncestor(root, p, q):
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)    
    elif root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)    
    else: # the split happened, since p and q are in different subtrees
        return root

# find the split approach, iterative
def lowestCommonAncestor2(root, p, q):
    current = root

    while current:
        if current.val < p.val and current.val < q.val: # both p and q are in right subtree
            current = current.right    
        elif current.val > p.val and current.val > q.val: # both p and q are in left subtree
            current = current.left
        else: # the split happened, since p and q are in different subtrees
            return current

# dfs approach
def lowestCommonAncestor3(root, p, q):
    if root == None: # empty node
        return None
    
    if root.val == p.val or root.val == q.val: # found p or q
        return root

    left = lowestCommonAncestor(root.left, p, q) # found p or q in left subtree
    right = lowestCommonAncestor(root.right, p, q) # found p or q in right subtree

    if left and right: # p and q are in different subtrees
        return root
    if left != None: # p and q are in the same subtree
        return left
    else:
        return right