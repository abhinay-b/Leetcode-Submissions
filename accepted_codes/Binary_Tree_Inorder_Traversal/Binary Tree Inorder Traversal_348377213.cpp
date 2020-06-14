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
/*
 * Iterative traversal:
 * Keep traversing to the left and store the current node to stack till there's no left
 * Pop from stack and print the node. Go to its right node
 * Repeat the above process
*/
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> stk;
        vector<int> res;
        while(root || stk.size())
        {
            if(root)
            {
                stk.push(root);
                root = root->left;
            }
            else
            {
                root = stk.top();
                stk.pop();
                res.push_back(root->val);
                root = root->right;
            }  
        }
        
        return res;
    }
};
