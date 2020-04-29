# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        def maxDepth(root):
            if not root:
                return 0,0
            depth1,diameter1 = maxDepth(root.left)
            depth2,diameter2 = maxDepth(root.right)
            diameter = max(diameter1,diameter2,depth1+depth2)
            return (1+max(depth1,depth2),diameter)
        return maxDepth(root)[1]
