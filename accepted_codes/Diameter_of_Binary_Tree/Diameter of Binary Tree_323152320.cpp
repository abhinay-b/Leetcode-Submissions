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
    pair<int,int>helper(TreeNode *root)
    {
        if(root == NULL)
            return pair(0,0);
        auto [leftMax, left] = helper(root->left);
        auto [rightMax, right] = helper(root->right);
        return(pair(max(left+right,max(leftMax,rightMax)), max(left,right)+1));
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        return helper(root).first;
        
    }
};
