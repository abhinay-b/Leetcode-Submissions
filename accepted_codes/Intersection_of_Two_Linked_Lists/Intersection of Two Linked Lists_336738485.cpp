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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int countA = 0,countB = 0;
        auto temp = headA;
        while(temp)
        {
            temp = temp->next;
            countA++;
        }
        temp = headB;
        while(temp)
        {
            temp = temp->next;
            countB++;
        }
        
        if(countA < countB)
        {
            temp = headA;
            headA = headB;
            headB = temp;
            countA = countA ^ countB;
            countB = countA ^ countB;
            countA = countA ^ countB;
        }
        while(countA > countB)
        {
            headA = headA->next;
            countA--;
        }
        while(headA)
        {
            if(headA == headB)
                return headA;
            headA = headA->next;
            headB = headB->next;
        }
        return NULL;
        
    }
};
