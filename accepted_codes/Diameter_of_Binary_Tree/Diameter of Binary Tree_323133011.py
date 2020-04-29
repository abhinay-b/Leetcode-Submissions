# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def helper(root):
#           return maxPath, maxBranch
            if not root:
                return 0,0
            leftMax, left = helper(root.left)
            rightMax, right = helper(root.right)
            return(max(leftMax,rightMax,left+right),max(left,right)+1)
        res,_ = helper(root)
        return res
