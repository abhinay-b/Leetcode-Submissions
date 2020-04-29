# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev,nxt = dummy,dummy
        count = 0
        while count < n and nxt.next:
            if count == m-1:
                prev = nxt
                nxt = nxt.next
            elif count >= m:
                temp = nxt.next.next
                nxt.next.next = prev.next
                prev.next = nxt.next
                nxt.next = temp
            else:
                nxt = nxt.next
            count += 1
        return dummy.next
