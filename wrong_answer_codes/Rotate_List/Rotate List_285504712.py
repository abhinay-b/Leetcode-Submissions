# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = 1
        temp = head
        if not head or head.next == None:
            return head
        while temp.next != None:
            temp = temp.next
            length += 1
        last = temp
        count = 1
        temp = head
        if k >= length:
            k -= length
        while count < (length-k):
            temp = temp.next
            count += 1
        last.next = head
        head = temp.next
        temp.next = None
        return head
