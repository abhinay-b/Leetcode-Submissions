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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root)
            return {};
        vector<vector<int>>res;
        std::deque<pair<TreeNode*,int>> queue;
        queue.push_back(pair(root,0));
        while(queue.size() > 0)
        {
            auto [node,depth] = queue.front();
            queue.pop_front();
            if(res.size() == depth)
                res.push_back({});
            res[depth].push_back(node->val);
            if(node->left)
                queue.push_back(pair(node->left,depth+1));
            if(node->right)
                queue.push_back(pair(node->right,depth+1));
        }
        return res;
    }
};
