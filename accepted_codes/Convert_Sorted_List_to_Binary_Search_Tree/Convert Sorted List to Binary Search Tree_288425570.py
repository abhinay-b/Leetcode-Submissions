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
        def inorder(n):
            nonlocal head
            if n <= 0:
                return None
            left= inorder(n//2)
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = inorder((n-1)//2)
            return root
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return inorder(count)
