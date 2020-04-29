# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(root,add):
            if not root:
                return 0
            add = add*10 + root.val
            if not root.left and not root.right:
                return add
            return helper(root.left,add) + helper(root.right,add)
        return helper(root,0)
