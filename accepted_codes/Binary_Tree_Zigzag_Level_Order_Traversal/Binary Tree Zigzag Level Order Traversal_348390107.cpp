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
 * Do a BFS traversal and push into a queue: (node,depth)
 * Maintain a list of lists to store results
 * For odd depths, push front into the corresponding list
 * For even depths, push back into the corresponding lists
*/
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        
        vector<list<int>>res;
        deque<pair<TreeNode*,int>>q;
        if(!root)
            return {};
        q.push_back(pair(root,0));
        while(q.size())
        {
            auto [node,depth] = q.front();
            q.pop_front();
            if(res.size() == depth)
            {
                res.push_back({});
            }
            if(depth%2)
                res[depth].push_front(node->val);
            else
                res[depth].push_back(node->val);
            if(node->left)
                q.push_back(pair(node->left,depth+1));
            if(node->right)
                q.push_back(pair(node->right,depth+1));
                
        }
        vector<vector<int>>result;
        int len =0;
        for(auto &lst: res)
        {
            result.push_back({});
            for(auto &elem : lst)
                result[len].push_back(elem);
            len++;
        }
        return result;
    }
};
