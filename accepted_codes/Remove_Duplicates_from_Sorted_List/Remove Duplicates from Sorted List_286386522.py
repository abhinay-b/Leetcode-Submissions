# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev,temp = head,head
        while temp:
            while temp.next and temp.val == temp.next.val:
                temp = temp.next
            temp = temp.next
            prev.next = temp
            prev = temp
        return head
