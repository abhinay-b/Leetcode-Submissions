# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def checkBST(root, minVal,maxVal):
            if root == None:
                return True
            val = minVal < root.val < maxVal
            if not val:
                return val
            lval = checkBST(root.left,minVal,root.val)
            if not lval: 
                return lval
            rval = checkBST(root.right, root.val, maxVal)
            return rval
        return checkBST(root,-float('inf'),float('inf'))
        
