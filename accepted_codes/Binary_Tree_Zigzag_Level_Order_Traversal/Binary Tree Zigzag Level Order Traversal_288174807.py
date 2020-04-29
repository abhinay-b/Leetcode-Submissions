# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections 
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res= []
        if not root:
            return res
        q = []
        temp = [(root,0)]
        while temp:
            num,depth = temp.pop(0)
            if num.left:
                temp.append((num.left,depth+1))
            if num.right:
                temp.append((num.right,depth+1))
            if len(q) < depth+1:
                q.append(collections.deque())
            if depth%2:
                q[depth].appendleft(num.val)
            else:
                q[depth].append(num.val)
        return [i for i in q]
                    
