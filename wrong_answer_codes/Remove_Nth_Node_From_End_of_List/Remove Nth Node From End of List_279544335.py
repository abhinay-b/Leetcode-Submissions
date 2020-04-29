# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        length = 1
        while(temp != None):
            length += 1
            temp = temp.next
        pos = length - n
        if pos == 0:
            head = head.next
            return head
        temp = prev = head
        count = 1
        while temp!= None and count < pos:
            prev = temp
            count += 1
            temp = temp.next
        prev.next = temp.next
        return head
