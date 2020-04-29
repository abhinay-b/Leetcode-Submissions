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
            last = None
            while stack and num > stack[-1].val:
                #should come to left of num
                #numbers in stack will be in increasing order(LIFO)
                stack[-1].right = last
                last = stack.pop()
            node = TreeNode(num)
            node.left = last
            stack.append(node)
        if stack:
            last = None
        while stack:
            #numbers in stack will be in increasing order(LIFO)
            stack[-1].right = last
            last = stack.pop()
        return last
