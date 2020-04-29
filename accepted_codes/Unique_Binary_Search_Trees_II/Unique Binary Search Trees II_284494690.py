# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        res = []
        
        def traversal(elem,left,right):
            sub,leftSub,rightSub = [],[],[]
            head = None
            for idx,ele in enumerate(left):
                if len(left) > 1:
                    leftSub += traversal(ele,left[:idx],left[idx+1:])
                else:
                    leftSub = [TreeNode(ele)]
                
            for idx,ele in enumerate(right):
                if len(right) > 1:
                    rightSub += traversal(ele,right[:idx],right[idx+1:])
                else:
                    rightSub = [TreeNode(ele)]
            i = j = 0
            while i < len(leftSub):
                j = 0
                while j < len(rightSub):
                    head = TreeNode(elem) 
                    head.left = leftSub[i]
                    head.right = rightSub[j]
                    sub.append(head)
                    j += 1
                i += 1
            if len(rightSub) == 0:
                i = 0
            while i < len(leftSub):
                head = TreeNode(elem)
                head.left = leftSub[i]
                sub.append(head)
                i += 1

            while j < len(rightSub):
                head = TreeNode(elem)
                head.right = rightSub[j]
                sub.append(head)
                j += 1
            return sub
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]
        nums = range(1,n+1)
        for idx,ele in enumerate(nums):
            res += traversal(ele,nums[:idx],nums[idx+1:])
        return res
