# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeftMost(self,root,prev):
        if not root:
            return None
        if not root.left and not root.right:
            prev.right = None
            return root
        if root.right:
            return self.findLeftMost(root.right,root)
        return None
    
    def helper(self,root,key):
        if not root:
            return False,root,False
        if root.val == key:
            node = self.findLeftMost(root.left,root.left)
            if node:
                node.right = root.right
                if node != root.left: 
                    node.left = root.left
                root.left = None
                root.right = None
            return False,node,True
        flag1,node,flag2 = self.helper(root.left,key)
        if flag1:
            return flag1,node,flag2
        if flag2:
            if node:
                root.left = node
            else:
                root.left = root.left.right
            flag1 = True
            return flag1,node,flag2
        flag1,node,flag2 = self.helper(root.right,key)
        if flag1:
            return flag1,node,flag2
        if flag2:
            if node:
                root.right = node
            else:
                root.right = root.right.right
            flag1 = True
        return flag1,node,flag2
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        flag1,node,flag2 = self.helper(root,key)
        if not flag1 and flag2:
            if node:
                return node
            if root.right:
                root.right.left = root.left
            return root.right
        return root
            
