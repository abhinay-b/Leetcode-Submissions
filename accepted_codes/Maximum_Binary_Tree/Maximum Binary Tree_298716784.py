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
        idx = nums.index(max(nums))
        node = TreeNode(nums[idx])
        node.left = self.constructMaximumBinaryTree(nums[0:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return node
