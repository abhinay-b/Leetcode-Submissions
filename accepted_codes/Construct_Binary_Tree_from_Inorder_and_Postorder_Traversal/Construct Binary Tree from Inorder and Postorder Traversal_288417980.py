# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(start1,end1,start2,end2):
            if start1 > end1:
                return
            val = postorder[end2]
            root = TreeNode(val)
            idx = inorderDictn[val]
            root.left = build(start1,idx-1,start2,start2+(idx-1-start1))
            root.right = build(idx+1,end1,start2+(idx-start1),end2-1)
            return root
        inorderDictn = defaultdict(int)
        for idx,entry in enumerate(inorder):
            inorderDictn[entry] = idx
        return build(0,len(postorder)-1,0,len(inorder)-1)
