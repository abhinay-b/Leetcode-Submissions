/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto dummy = ListNode(-1, head);
        auto slow = &dummy, fast = head;
        int count = 0;
        while(fast && count < n)
        {
            fast = fast->next;
            count++;  
        }
        while(fast)
        {
            fast = fast->next;
            slow = slow->next;
        }
        auto temp = slow;
        slow->next = slow->next->next;
        return dummy.next;
    }
};
