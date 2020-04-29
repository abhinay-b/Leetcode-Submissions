# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder,inorder,start,end):
            if not preorder:
                return
            val = preorder[0]
            idx1 = inorderDict[val]
            root = TreeNode(val)
            root.left = build(preorder[1:(idx1-start)+1],inorder,start,idx1-1)
            root.right = build(preorder[(idx1-start)+1:],inorder,idx1+1,end)
            return root
        inorderDict = defaultdict()
        for idx,entry in enumerate(inorder):
            inorderDict[entry] = idx
        return build(preorder,inorder,0,len(inorder)-1)
