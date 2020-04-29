# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        prev = None
        odd = head
        even = head.next
        while odd != None and even != None:
            odd.next = even.next
            even.next = odd
            if prev != None:
                prev.next = even
            else:
                head = even
            prev = odd
            odd = odd.next
            if odd == None:
                break
            even = odd.next
        return head
