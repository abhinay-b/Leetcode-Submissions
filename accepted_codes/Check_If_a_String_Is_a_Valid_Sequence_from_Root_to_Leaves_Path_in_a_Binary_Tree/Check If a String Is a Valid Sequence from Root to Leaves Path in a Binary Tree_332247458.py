# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root: 
            return len(arr) == 0
        
        if not root.left and not root.right:
            if len(arr) != 1:
                return False
            return root.val == arr[0]
        
        if not arr:
            return False        
        
        if root.val == arr[0]:
            if root.left and self.isValidSequence(root.left,arr[1:]):
                return True
            if root.right:
                return self.isValidSequence(root.right,arr[1:])
        return False
