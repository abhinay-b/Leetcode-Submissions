# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        temp = []
        def helper(root,temp):
            if not root:
                return
            if not root.left and not root.right:
                temp += str(root.val)
                res.append(temp)
                return 
            temp += str(root.val) + "->"
            helper(root.left,temp)
            helper(root.right,temp)
        helper(root,"")
        return res
