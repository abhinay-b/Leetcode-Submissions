/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    int count = 0;
public:
    int kthSmallest(TreeNode* root, int k) {
        if(root == NULL)
            return 0;
        int val = kthSmallest(root->left, k);
        if (this->count == k)
            return val;
        this->count++;
        if(this->count == k)
            return root->val;
        return kthSmallest(root->right,k);
        
    }
};
