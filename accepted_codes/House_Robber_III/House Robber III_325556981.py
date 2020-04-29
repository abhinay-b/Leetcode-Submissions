from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:        
        def helper(root):
            if not root:
                return 
            val = root.val
            helper(root.left)
            helper(root.right)
            if root.left:
                val += dictn[root.left.left] + dictn[root.left.right]
            if root.right:
                val += dictn[root.right.left] + dictn[root.right.right]
            dictn[root] = max(val, dictn[root.left]+dictn[root.right])
             
        dictn = defaultdict(int)
        helper(root)
        return dictn[root]
