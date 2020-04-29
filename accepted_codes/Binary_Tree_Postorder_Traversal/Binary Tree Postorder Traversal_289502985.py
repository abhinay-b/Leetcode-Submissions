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
        visited = set()
        while stack:
            temp = stack.pop()
            if (temp.left and temp.left not in visited) or (temp.right and temp.right not in 
                visited):
                stack.append(temp)
            else:
                visited.add(temp)
                res.append(temp.val)
            if temp.right and temp.right not in visited:
                stack.append(temp.right)
            if temp.left and temp.left not in visited:
                stack.append(temp.left)
        return res
