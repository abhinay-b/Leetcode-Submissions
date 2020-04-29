# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def helper(root):
#           return maxPath, maxPathList, maxBranch, maxBranchList
            if not root:
                return 0, [], 0, []
            path1, path1L, left, leftList = helper(root.left) 
            path2, path2L, right, rightList = helper(root.right)
            currentPath = left+right+root.val
            
            if path1 < path2 or (path1 == path2 and len(path1L) < len(path2L)):
                path1,path2 = path2,path1
                path1L,path2L = path2L, path1L
         
            if left < right or left == right and len(leftList) < len(rightList):
                left, right = right,left
                leftList, rightList = rightList, leftList
                
            if currentPath > path1:
                return (currentPath, leftList+rightList+[root.val], left+root.val, leftList
                    +[root.val])
            return(path1, path1L, left+root.val, leftList+[root.val])
        _,res,_,_ = helper(root)
        # print(res)
        return max(len(res)-1,0)
