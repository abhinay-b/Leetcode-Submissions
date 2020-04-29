# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        while curr.next:
            temp = curr.next
            curr.next = curr.next.next
            temp.next = dummy.next
            dummy.next = temp
        return dummy.next
            
