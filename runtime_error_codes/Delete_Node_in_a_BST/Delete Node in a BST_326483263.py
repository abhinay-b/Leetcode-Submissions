# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findRightMost(self,root,prev):
        if not root:
            return None
        if not root.left and not root.right:
            prev.right = None
            return root
        if root.right:
            return self.findRightMost(root.right,root)
        if prev:
            prev.right = root.left
        return root
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val == key:
#           find the rightmost node in the left subtree
            node = self.findRightMost(root.left,None)
#           if there is a left subtree, the node will have no right children
            if node:
                node.right = root.right
                if node != root.left: 
                    node.left = root.left
#           if there is not left subtree, the node will be the right child
            else:
                node = root.right  
            # print('new node:',node)
            return node
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        return root
            
