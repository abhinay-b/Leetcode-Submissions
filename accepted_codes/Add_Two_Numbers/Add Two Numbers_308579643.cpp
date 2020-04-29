/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        auto head1 = l1, head2 = l2;
        auto head3 = new ListNode(-1);
        auto temp = head3;
        auto sum = 0, carry = 0;
        while(head1 and head2)
        {            
            sum = head1->val+head2->val+carry;
            carry = sum / 10;
            auto newNode = new ListNode(sum % 10); 
            temp->next = newNode;
            temp = temp->next;
            head1 = head1->next;
            head2 = head2->next;
        }
        while(head1)
        {
            sum = head1->val+carry;
            carry = sum / 10;
            auto newNode = new ListNode(sum % 10); 
            temp->next = newNode;
            temp = temp->next;
            head1 = head1->next;
        }
        while(head2)
        {
            sum = head2->val+carry;
            carry = sum / 10;
            auto newNode = new ListNode(sum % 10); 
            temp->next = newNode;
            temp = temp->next;
            head2 = head2->next;   
        }
        if(carry)
        {
            auto newNode = new ListNode(carry); 
            temp->next = newNode;
        }
            
        return head3->next;
    }
};
