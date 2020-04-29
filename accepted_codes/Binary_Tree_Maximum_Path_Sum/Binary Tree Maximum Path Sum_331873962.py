# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxVal = -float('inf')
        def helper(root):
            nonlocal maxVal
            if not root:
                return 0
            leftPath = helper(root.left)
            rightPath = helper(root.right)
            maxChild = max(root.val,root.val+max(leftPath,rightPath))
            maxVal = max(maxVal,maxChild,root.val+leftPath + rightPath)
            return maxChild
        helper(root)
        return maxVal
