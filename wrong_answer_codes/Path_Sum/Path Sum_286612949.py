# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        def checkSum(root,sum):
            if not root:
                if sum != 0:
                    return False
                return True
            sum -= root.val
            if sum < 0:
                return False
            return checkSum(root.left,sum) or checkSum(root.right,sum)
        return checkSum(root,sum)
