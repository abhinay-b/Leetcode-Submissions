# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 
        'TreeNode':
        def Helper(root,p,q):
            if not root:
                return None,False
            val0,flag0 = None,False
            if root == p and root == q:
                return root,True
            if root == p or root == q:
                val0,flag0 = None,True
            val1,flag1 = Helper(root.left,p,q)
            val2,flag2 = Helper(root.right,p,q)
            if val1:
                return val1,True
            if val2:
                return val2,True
            if not (flag0 | flag1 | flag2):
                return (None,False)
            if flag0 ^ flag1 ^ flag2:
                return (None,True)
            return (root,True)
        return Helper(root,p,q)[0]
