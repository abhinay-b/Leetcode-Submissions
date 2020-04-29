# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while len(stack) > 0:            
            while len(stack) > 0:
                temp = stack[-1]                
                temp = temp.left
                if temp != None:
                    if temp.left or temp.right:
                        stack.append(temp)
                        continue
                    else:
                        res.append(temp.val)
                        break
                else:
                    break
            while len(stack) > 0:
                temp = stack.pop()
                res.append(temp.val)
                temp = temp.right
                if temp:
                    if temp.left or temp.right:
                        stack.append(temp)
                        break
                    else:
                        res.append(temp.val)
        return res
