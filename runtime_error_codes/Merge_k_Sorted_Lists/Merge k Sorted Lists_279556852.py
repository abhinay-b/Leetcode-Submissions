# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def combo(l1,l2):
            # l1 = lists[0]
            # l2 = lists[1]
            l3 = None
            # print(type(l1))
            while l1 != None and l2 != None:
                if l1.val <= l2.val:
                    newNode = l1
                    l1 = l1.next
                else:
                    newNode = l2
                    l2 = l2.next
                if l3 == None:
                    l3 = newNode
                    temp = l3
                else:
                    temp.next = newNode
                    temp = temp.next
            if l1 != None:
                newNode = l1
            elif l2 != None:
                newNode = l2
            if l3 == None:
                l3 = newNode
            else:
                temp.next = newNode
            return l3
        
        def merge(lists):
            if len(lists) == 1:
                return lists[0]
            elif len(lists) == 2:
                return combo(lists[0],lists[1])
            else:
                l1 = merge(lists[:len(lists)//2])
                l2 = merge(lists[len(lists)//2:])
                return combo(l1,l2)
        return merge(lists)
