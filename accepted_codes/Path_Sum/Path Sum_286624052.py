# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, temp: TreeNode, sum: int) -> bool:
        if not temp:
            return False
        def checkSum(root,sum):            
            if not root:
                if sum != 0:
                    return False
                return True
            sum -= root.val
            val = False
            if root.left and root.right:
                return checkSum(root.left,sum) or checkSum(root.right,sum)
            if root.left:
                return checkSum(root.left,sum)
            return checkSum(root.right,sum)
        return checkSum(temp,sum)
