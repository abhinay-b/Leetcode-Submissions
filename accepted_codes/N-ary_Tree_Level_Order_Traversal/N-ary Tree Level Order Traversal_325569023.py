from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root,0)])
        res = []
        
        while queue:
            node,depth = queue.popleft()
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            for child in node.children:
                    queue.append((child,depth+1))
        return res
