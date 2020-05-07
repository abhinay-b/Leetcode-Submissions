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
    ListNode* reverseList(ListNode* head) {
        auto dummy = ListNode(-1,head);
        auto temp = head;
        while(head->next != nullptr)
        {
            temp = head->next;
            head->next = head->next->next;
            temp->next = dummy.next;
            dummy.next = temp;
            
        }
        return dummy.next;
    }
};
