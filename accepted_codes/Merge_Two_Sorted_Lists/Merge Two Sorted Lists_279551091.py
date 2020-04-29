# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = None
        temp = l3
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                newNode = l1
                l1 = l1.next
            else:
                newNode = l2
                l2 = l2.next
            newNode.next = None
            if(l3 == None):
                l3 = newNode
                temp = l3
            else:
                temp.next = newNode
                temp = temp.next
        if l1 != None:
            if(l3 == None):
                l3 = l1
                temp = l3
            else:
                temp.next = l1
        elif l2 != None:
            if(l3 == None):
                l3 = l2
            else:
                temp.next = l2
        return l3
