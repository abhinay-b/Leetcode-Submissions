# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        countA,countB = 0,0
        tempA,tempB = headA,headB
        while tempA:
            tempA = tempA.next
            countA += 1
        while tempB:
            tempB = tempB.next
            countB += 1
        if countB > countA:
            headA,headB = headB,headA
            countA,countB = countB,countA
        tempA,tempB = headA,headB
        while countA - countB > 0:
            tempA = tempA.next
            countA -= 1
        while tempA and tempB:
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next
        return None
       
