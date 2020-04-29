from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:        
        def helper(root, dictn):
            if not root:
                return dictn
            val = root.val
            dictn = helper(root.left,dictn)
            dictn = helper(root.right,dictn)
            if root.left:
                val += dictn[root.left.left] + dictn[root.left.right]
            if root.right:
                val += dictn[root.right.left] + dictn[root.right.right]
            dictn[root] = max(val, dictn[root.left]+dictn[root.right])
            return dictn
        dictn = defaultdict(int)
        dictn = helper(root,dictn)
        return dictn[root]
