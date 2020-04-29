# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev,nxt = None, head
        while nxt:
            if nxt.next:
                if nxt.val != nxt.next.val:
                    if not prev:
                        head = nxt
                    prev = nxt
                    nxt = nxt.next
                else:
                    while(nxt.next and nxt.val == nxt.next.val):
                        nxt = nxt.next
                    nxt = nxt.next
            else:
                if prev.val != nxt.val:
                    prev.next = nxt
                    nxt = nxt.next
        if not prev:
            return prev
        return head
