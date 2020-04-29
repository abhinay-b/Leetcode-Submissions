# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def checkLevel(root):
            if not root:
                return 0
            lval = checkLevel(root.left)
            rval = checkLevel(root.right)
            if lval == -1 or rval == -1:
                return -1
            if abs(lval-rval) > 1:
                return -1
            return 1+max(lval,rval)
        return checkLevel(root) != -1
