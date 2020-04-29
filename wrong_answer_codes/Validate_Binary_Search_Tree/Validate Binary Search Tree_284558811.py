# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def checkRight(node,nList):
            if not node:
                return True
            if node.val <= min(nList):
                return False
            if node.right and node.right.val <= node.val:
                return False
            if node.left and node.left.val >= node.val:
                return False
            return (checkRight(node.left,nList+[node.val])) and (checkRight(node.right,nList
                +[node.val]))
        def checkLeft(node,nList):
            if not node:
                return True
            if node.val >= max(nList):
                return False
            if node.right and node.right.val <= node.val:
                return False
            if node.left and node.left.val >= node.val:
                return False
            return (checkLeft(node.left,nList+[node.val])) and (checkLeft(node.right,nList
                +[node.val]))
        if not root:
            return True
        return checkLeft(root.left,[root.val]) and (checkRight(root.right,[root.val]))
