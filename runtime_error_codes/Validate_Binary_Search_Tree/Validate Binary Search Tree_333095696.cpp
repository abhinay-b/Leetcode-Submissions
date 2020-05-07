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
public:
    bool isValidBST(TreeNode* root, pair<int,int>range = pair(INT_MIN,INT_MAX)) {
        if(!root)
            return true;
        if(range.first <= root->val && root->val <= range.second)
            return isValidBST(root->left,pair(range.first,root->val-1)) && isValidBST(root
                ->right,pair(root->val+1, range.second));
        return false;
    }
};
