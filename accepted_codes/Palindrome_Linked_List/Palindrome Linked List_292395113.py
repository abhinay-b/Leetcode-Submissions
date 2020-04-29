# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(node):
            prev,curr,nxt = None,node,node.next
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        def isSame(node1,node2):
            while node1 and node2:
                if node1.val == node2.val:
                    node1 = node1.next
                    node2 = node2.next
                else:
                    return False
            if node1 or node2:
                return False
            return True
        if not head or not head.next:
            return True
        prev,slow,fast = None,head,head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        head1,head2 = head,slow
        if fast:
            head2 = slow.next
        prev.next = None
        head2 = reverse(head2)
        return isSame(head1,head2)
