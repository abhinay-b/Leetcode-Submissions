from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root,0)])
        nums = []
        while queue:
            node, val = queue.popleft()
            if len(nums)-1 < val:
                nums.append(0)
            nums[val]+= node.val
            if node.left:
                queue.append((node.left,val+1))
            if node.right:
                queue.append((node.right,val+1))
        # print(nums)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        first,second = nums[0],nums[1]
        for i in range(2,len(nums)):
            if not i%2:
                second = max(first,second)
                first += nums[i]
            else:
                first = max(first,second)
                second += nums[i]
        return max(first,second)
