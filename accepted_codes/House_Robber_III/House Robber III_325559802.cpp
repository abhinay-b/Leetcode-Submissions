/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    unordered_map<TreeNode*,int> dictn;
public:
    void helper(TreeNode * root)
    {
        if(root == NULL)
        {
            return;
        }
        helper(root->left);
        helper(root->right);
        int val = root->val;
        if(root->left)
        {
            val += dictn[root->left->left] + dictn[root->left->right];
        }
        if(root->right)
        {
            val += dictn[root->right->left] + dictn[root->right->right];
        }
        dictn[root] = max(val, dictn[root->left]+dictn[root->right]);
    }
    int rob(TreeNode* root) {
        if (root == NULL) return 0;
        helper(root);
        return dictn[root];
    }   
};
