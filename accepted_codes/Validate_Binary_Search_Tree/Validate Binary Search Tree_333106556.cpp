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
    bool isValidBST(TreeNode* root, int *lower = NULL, int *upper = NULL) {
        if(!root)
            return true;
        if(lower && *lower >= root->val )
            return false;
        if(upper && *upper <= root->val)
            return false;
        return isValidBST(root->left,lower,&(root->val)) && isValidBST(root->right,&(root->val
            ), upper);
    }
};
