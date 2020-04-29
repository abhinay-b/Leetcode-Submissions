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
        def sll(root,temp):
            if not root:
                return temp
            right = None
            if temp != root:
                temp.right = root
                right = root.right
            else:
                right = temp.right
            temp = root
            temp = sll(root.left,temp)
            temp = sll(right,temp)
            root.left = None
            return temp
        sll(root,root)
