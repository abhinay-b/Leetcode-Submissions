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
        def buildTree(left,right):
            if left == right:
                return TreeNode(nums[left])
            if left == right-1:
                temp = TreeNode(nums[left])
                temp.right = TreeNode(nums[right])
                return temp
            mid = (left+right) // 2
            root = TreeNode(nums[mid])
            root.left = buildTree(left,mid-1)
            root.right = buildTree(mid+1,right)
            return root
        return buildTree(0,len(nums)-1)
