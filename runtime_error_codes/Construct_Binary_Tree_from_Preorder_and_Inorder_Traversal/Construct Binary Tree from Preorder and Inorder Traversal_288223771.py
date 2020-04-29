# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder,inorder):
            if not inorder:
                return
            val = preorder[0]
            idx1 = inorderDict[val]
            idx2 = idx1
            root = TreeNode(val)
            root.left = build(preorder[1:idx2+1],inorder[:idx1])
            root.right = build(preorder[idx2+1:],inorder[idx1+1:])
            return root
        inorderDict = defaultdict()
        for idx,entry in enumerate(inorder):
            inorderDict[entry] = idx
        return build(preorder,inorder)
