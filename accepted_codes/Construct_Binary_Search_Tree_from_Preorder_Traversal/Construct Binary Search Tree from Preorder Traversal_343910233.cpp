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
    TreeNode *helper(vector<int>& preorder, int beginIdx, int endIdx)
    {
        if(beginIdx >= endIdx)
            return NULL;
        auto node = new TreeNode(preorder[beginIdx++]);
        int leftCount = beginIdx;
        while(leftCount < endIdx && preorder[leftCount] < node->val)
            leftCount++;
        node->left = helper(preorder, beginIdx, leftCount);
        node->right = helper(preorder, leftCount, endIdx);
        return node;
    }
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int len = preorder.size();
        if(len == 0)
            return NULL;
        return helper(preorder,0,len);
    }
};
