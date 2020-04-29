# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: 
            return []
        firstList = [(root,0)]
        q = []
        while firstList:
            num,depth = firstList.pop(0)
            if num.left:
                firstList.append((num.left,depth+1))
            if num.right:
                firstList.append((num.right,depth+1))
            if len(q)<depth+1:
                q.append(deque())
            q[depth].append(num.val)
        return [i for i in q]
