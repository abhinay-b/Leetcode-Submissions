from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        buff = [0]*2
        queue = deque([(root,0)])
        while queue:
            node, val = queue.popleft()
            buff[val%2]+= node.val
            if node.left:
                queue.append((node.left,val+1))
            if node.right:
                queue.append((node.right,val+1))
        return max(buff)
