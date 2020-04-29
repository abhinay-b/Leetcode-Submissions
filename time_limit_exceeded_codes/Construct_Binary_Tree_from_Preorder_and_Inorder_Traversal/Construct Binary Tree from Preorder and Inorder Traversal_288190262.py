# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return
        val = preorder[0]
        idx1 = inorder.index(val)
        idx2 = 0
        root = TreeNode(val)
        if idx1:
            temp = idx1+1
            while len(inorder[:idx1]) != len(preorder[1:idx2+1]):
                temp -= 1
                idx2 = preorder.index(inorder[temp-1])
            
        root.left = self.buildTree(preorder[1:idx2+1],inorder[:idx1])
        root.right = self.buildTree(preorder[idx2+1:],inorder[idx1+1:])
        return root
