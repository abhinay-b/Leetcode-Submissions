# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev,curr = head,head
        while curr and curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                prev = curr    
                curr = curr.next
                curr2,prev2 = head,None
                while curr2.val <= curr.val:
                    prev2 = curr2
                    curr2 = curr2.next
                prev.next = curr.next
                curr.next = curr2
                if curr2 == head:
                    head = curr
                else:
                    prev2.next = curr
                curr = prev
        return head
