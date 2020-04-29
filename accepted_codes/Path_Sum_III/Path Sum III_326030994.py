from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0    
    def pathSum(self, root: TreeNode, total: int) -> int:
        dictn = defaultdict(int)
        dictn[0] = 1
        def dfs(root,currSum):
            if not root:
                return 
            currSum += root.val
            self.res += dictn[currSum-total]
            dictn[currSum] += 1
            dfs(root.left,currSum)
            dfs(root.right,currSum)
            dictn[currSum] -= 1
        dfs(root,0)
        return self.res
