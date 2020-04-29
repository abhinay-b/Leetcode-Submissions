# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append((root,1))
        while queue:
            # print([temp[0].val for temp in queue])
            node,depth = queue.popleft()
            if len(res) < depth:
                res.append([])
            res[depth-1].append(node.val)
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        print(res)
        return res[::-1]
