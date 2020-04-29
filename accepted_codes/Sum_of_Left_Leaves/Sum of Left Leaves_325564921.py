from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root,'')])
        count = res = 0
        while queue:
            node, side = queue.popleft()
            if not node.left and not node.right and side == 'l':
                res += node.val
            if node.left:
                queue.append((node.left,'l'))
            if node.right:
                queue.append((node.right,'r'))
        return res
