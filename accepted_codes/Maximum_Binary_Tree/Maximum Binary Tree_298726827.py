# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        stack = []
        last = None
        for num in nums:
            while stack and stack[-1].val < num:
                last = stack.pop()
            node = TreeNode(num)
            if stack:
                stack[-1].right = node 
            if last:
                node.left = last
            stack.append(node)
            last = None
        return stack[0]
        
