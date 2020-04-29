# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        beginIdx = 1
        endIdx = 1
        while endIdx < len(preorder) and preorder[endIdx] < root.val:
            endIdx += 1
        root.left = self.bstFromPreorder(preorder[beginIdx:endIdx])
        root.right = self.bstFromPreorder(preorder[endIdx:])
        return root
