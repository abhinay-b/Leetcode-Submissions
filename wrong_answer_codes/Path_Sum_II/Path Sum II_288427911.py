# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def checkSum(root,target,temp):
            if target < 0 or not root:
                return
            
            val = root.val
            target -= val
            if not root.left and not root.right:
                if target == 0:
                    res.append(temp+[val])
                return
            checkSum(root.left,target,temp+[val])
            checkSum(root.right,target,temp+[val])
        res = []
        checkSum(root,sum,[])
        return res
