# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, total: int) -> int:
        def check(root,temp):
            if not root:
                return 0
            val = 0
            if root.val == temp:
                val += 1
            val += check(root.left,temp-root.val) + check(root.right,temp-root.val)
            return val
        def dfs(root,temp):
            if not root:
                return 0
            val = check(root,temp)
            val += dfs(root.left,temp) + dfs(root.right,temp)
            return val
        return dfs(root,total)
