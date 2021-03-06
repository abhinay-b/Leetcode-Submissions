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
    ListNode *reverse(ListNode*start,ListNode*end)
    {
        auto temp = start;
        auto dummy = ListNode(-1,start);
        while(start->next != end)
        {
            temp = start->next;
            start->next = start->next->next;
            temp->next = dummy.next;
            dummy.next = temp;
        }
        return dummy.next;
    }
public:
    bool isPalindrome(ListNode* head) {
        auto fast = head, slow = head;
        auto end = head, head2 = head;
        while(fast && fast->next)
        {
            fast = fast->next->next;
            slow = slow->next;
        }
        end = slow;
        if(fast)
        {
            head2 = slow->next;            
        }
        else
        {
            head2 = slow;
        }
        slow = reverse(head,end);
        
        while(slow != end && head2)
        {
            if(slow->val != head2->val)
                return false;
            slow = slow->next;
            head2 = head2->next;
        }
        return true;
    }
};
