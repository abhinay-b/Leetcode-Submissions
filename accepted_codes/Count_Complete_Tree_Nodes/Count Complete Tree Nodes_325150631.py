# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        leftMost,rightMost = 0,0
        curr = root
        while curr:
            leftMost += 1
            curr = curr.left
        curr = root
        while curr:
            rightMost += 1
            curr = curr.right
        if leftMost == rightMost:
            return 2**leftMost - 1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
