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
        dictn = dict()
        idx = 0
        temp = head
        while temp:
            dictn[idx] = temp
            idx += 1
            temp = temp.next
        count = idx-1
        if count <= 1:
            return head
        node = head        
        while node.next and node.next != dictn[count]:
            temp = node.next
            dictn[count-1].next = None
            node.next = dictn[count]            
            dictn[count].next = temp
            node = temp
            count -= 1
