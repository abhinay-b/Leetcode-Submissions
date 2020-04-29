# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import itertools as it
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumList = ListNode(-1)
        carry = 0
        total = sumList
        n1 = l1
        n2 = l2
        while n1 != None or n2 != None:
            value = carry
            if n1 != None:
                value += n1.val
                n1 = n1.next
            if n2 != None:
                value += n2.val
                n2 = n2.next
            carry = value // 10
            newNode = ListNode(value % 10)
            
            if(sumList.val == -1):
                total = newNode
                sumList = total
            else:
                sumList.next = newNode
                sumList = sumList.next
            
            
        if carry != 0:
            newNode = ListNode(carry)
            sumList.next = newNode
            sumList = sumList.next        
        
        return total
            
