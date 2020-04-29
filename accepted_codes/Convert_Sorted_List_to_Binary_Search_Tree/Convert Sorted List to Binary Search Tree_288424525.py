# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def inorder(head,n):
            if n <= 0:
                return None,head
            left,head = inorder(head,n//2)
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right,head = inorder(head,n-n//2-1)
            return root,head
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return inorder(head,count)[0]
