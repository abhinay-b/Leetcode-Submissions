# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev1,nxt1 = dummy,None
        prev2,nxt2 = dummy,head
        while nxt2:
            if nxt2.val >= x and not nxt1:
                prev1,nxt1 = prev2,nxt2
            elif nxt2.val < x and nxt1:
                prev1.next = nxt2
                prev1 = nxt2
                prev2.next = nxt2.next
                nxt2.next = nxt1
                nxt2 = prev2.next
                continue
            prev2 = nxt2
            nxt2 = nxt2.next
                
        return dummy.next
