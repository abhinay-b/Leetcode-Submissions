# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                if isMirror(p.left,q.right):
                    return isMirror(p.right,q.left)
        if not root:
            return True
        return isMirror(root.left,root.right)
