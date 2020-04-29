# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        left,right = 0,len(nums)-1
        leftNode, rightNode = None,None
        while left < mid or right > mid:
            if left < mid:
                temp = TreeNode(nums[left])
                temp.left = leftNode
                leftNode = temp
                left += 1
            if right > mid:
                temp = TreeNode(nums[right])
                temp.right = rightNode
                rightNode = temp
                right -= 1
            
        root.left = leftNode
        root.right = rightNode
        return root
