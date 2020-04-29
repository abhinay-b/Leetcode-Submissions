# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(start1,end1,start2,end2):
            if start1 > end1:
                return
            val = preorder[start2]
            idx1 = inorderDict[val]
            root = TreeNode(val)
            root.left = build(start1,idx1-1,start2+1,start2+(idx1-start1))
            root.right = build(idx1+1,end1,start2+1+(idx1-start1),end2)
            return root
        inorderDict = defaultdict()
        for idx,entry in enumerate(inorder):
            inorderDict[entry] = idx
        return build(0,len(inorder)-1,0,len(preorder)-1)
