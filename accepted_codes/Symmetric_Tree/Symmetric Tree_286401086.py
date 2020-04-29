# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        firstList = [root]
        while firstList:
            for i in range(len(firstList)//2):
                if firstList[i] == None and firstList[-i-1] == None:
                    continue
                if firstList[i] == None or firstList[-i-1] == None:
                    return False
                if firstList[i].val != firstList[-i-1].val:
                    return False
            secondList = []
            for temp in firstList:
                if temp:
                    secondList.append(temp.left)
                    secondList.append(temp.right)
            firstList = secondList
        return True
            
