# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev,curr = head,head.next
        while curr:
            curr2,prev2 = head,None
            while curr2 != curr:
                if curr.val < curr2.val:
                    prev.next = curr.next
                    curr.next = curr2
                    if curr2 == head:
                        head = curr
                    else:
                        prev2.next = curr
                    break
                prev2 = curr2
                curr2 = curr2.next
            if curr2 == curr:
                prev = curr
                curr = curr.next
            else:
                prev = curr2
                curr = curr2.next
        return head
