# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        slow,fast = head,head
#         reach mid point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
#         reverse the linked list from mid to end
        prev,curr = head2,head2.next
        while curr:
            prev.next = curr.next
            curr.next = head2
            head2 = curr
            curr = prev.next
#           merge the 2 lists into one
        curr1,curr2 = head,head2
        while curr1 and curr2:
            temp1 = curr1.next
            curr1.next = curr2
            temp2 = curr2.next
            curr2.next = temp1
            curr2 = temp2
            curr1 = temp1
        
