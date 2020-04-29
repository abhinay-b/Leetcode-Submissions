# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def sll(child,parent):
            if not child:
                return parent
            if parent != child:
                parent.right = child
            right = child.right
            parent = sll(child.left,child)
            parent = sll(right,parent)
            child.left = None
            return parent
        sll(root,root)
