from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = deque([root])
        res = []
        while stack:
            temp = stack.pop()
            if temp.left or temp.right:
                stack.append(temp)
            else:
                res.append(temp.val)
            if temp.right:
                stack.append(temp.right)
                temp.right = None
            if temp.left:
                stack.append(temp.left)
                temp.left = None
        return res
