# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, child: TreeNode, parent=None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not child:
            return parent
        if parent:
            parent.right = child
        right = child.right
        temp = self.flatten(child.left,child)
        temp = self.flatten(right,temp)
        child.left = None
        return temp

