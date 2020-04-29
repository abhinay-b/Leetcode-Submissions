# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
        if root.left:
            return 1+self.minDepth(root.left)
        return 1+self.minDepth(root.right)
