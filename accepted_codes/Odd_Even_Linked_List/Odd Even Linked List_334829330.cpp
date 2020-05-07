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
    ListNode* oddEvenList(ListNode* head) {
        if(!head || !(head->next) || !(head->next->next))
            return head;
        ListNode* odd = head, *prev;
        ListNode*even = new ListNode(-1);
        ListNode *temp = even;
        while(odd && odd->next)
        {
            temp->next = odd->next;
            odd->next = odd->next->next;
            temp = temp->next;
            prev = odd;
            odd = odd->next;
        }
        if(!odd)
            odd = prev;
        //Ensure that the last even node doesn't point anymore to the next odd node, if any, 
            to avoid cycle! 
        temp->next = NULL;
        odd->next = even->next;
        return head;
    }
};
