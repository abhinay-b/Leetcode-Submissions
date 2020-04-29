# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: 
            return []
        firstList = [root]
        res = []
        while firstList:
            secondList,temp = [],[]
            for node in firstList:
                temp.append(node.val)
                if node.left:
                    secondList.append(node.left)
                if node.right:
                    secondList.append(node.right)
            res.append(temp)
            firstList = secondList
        return res
