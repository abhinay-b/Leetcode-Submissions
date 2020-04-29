# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        prev,curr = [],[root]
        res = []
        while curr:
            res.append(curr[-1].val)
            for node in curr:
                if node.left:
                    prev.append(node.left)
                if node.right:
                    prev.append(node.right)
            curr = prev
            prev = []
        return res
