"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        temp = head
        while temp:
            dupe = Node(temp.val)
            dupe.next = temp.next
            temp.next = dupe
            temp = dupe.next
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        temp1 = head
        res,temp2 = head.next,head.next
        while temp1:
            if temp1.next:
                temp1.next = temp1.next.next
            if temp2.next:
                temp2.next = temp2.next.next
            temp1 = temp1.next
            temp2 = temp2.next
        return res
