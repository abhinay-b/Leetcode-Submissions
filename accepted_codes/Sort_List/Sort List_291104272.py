# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast,slow,prev = head,head,None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        prev,curr = None,l1
        while curr and l2:
            if curr.val <= l2.val:
                prev = curr
                curr = curr.next
            else:
                if prev:
                    prev.next = l2
                else:
                    l1 = l2
                temp = l2.next
                l2.next = curr
                prev = l2
                l2 = temp
        if l2:
            prev.next = l2
            prev = prev.next
        return l1
