# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        def helper(root, count):
            if not root:
                return count,-float('inf')
            count,val = helper(root.left, count)
            if count == k:
                return count,val
            count += 1
            if count == k:
                return count,root.val
            return helper(root.right,count)
        return helper(root,0)[1]
            
