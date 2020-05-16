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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *dummy = new ListNode(-1);
        auto *temp = dummy;
        int carry = 0, sum;
        while(l1 && l2)
        {
            sum = l1->val + l2->val + carry;
            temp->next = new ListNode(sum%10);
            carry = sum / 10;
            temp = temp->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        while(l1)
        {
            sum = l1->val + carry;
            temp->next = new ListNode(sum%10);
            carry = sum / 10;
            temp = temp->next;
            l1 = l1->next;
        }
        while(l2)
        {
            sum = l2->val + carry;
            temp->next = new ListNode(sum%10);
            carry = sum / 10;
            temp = temp->next;
            l2 = l2->next;
        }
        if(carry)
            temp->next = new ListNode(carry);
        return dummy->next;
        
    }
};
