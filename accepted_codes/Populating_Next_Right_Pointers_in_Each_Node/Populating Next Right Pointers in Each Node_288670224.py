"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = 
        None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        head = root
        while head:
            temp1 = head
            temp2 = None
            while temp1:                
                if temp1.left:
                    if not temp2:
                        temp2 = temp1.left
                    else:
                        temp2.next = temp1.left
                        temp2 = temp2.next
                    temp2.next = temp1.right
                    temp2 = temp2.next
                temp1 = temp1.next
            head = head.left
        return root
                
