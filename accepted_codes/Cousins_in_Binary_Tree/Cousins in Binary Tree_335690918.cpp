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
    bool isCousins(TreeNode* root, int x, int y) {
        if(!root || !root->left || !root->right)
            return false;
        std::deque<tuple<TreeNode*, int, int>> queue;
        queue.push_back(tuple(root,0,-1));
        std::vector<unordered_map<int,int>> levels(1);
        levels[0][root->val] = -1;
        while(queue.size() > 0)
        {
            auto [node,depth, parent] = queue.front();
            queue.pop_front();
            if(depth == levels.size())
            {
                // for(auto [key,val] : levels[depth-1])
                //     cout<<"key val: "<<key << val<<endl;
                if(levels[depth-1].find(x) != levels[depth-1].end())
                    break;
                levels.push_back({});
            }
            levels[depth][node->val] = parent;
            if(node->left)
                queue.push_back(tuple(node->left,depth+1,node->val));
            if(node->right)
                queue.push_back(tuple(node->right,depth+1,node->val));
        }
        auto depth = levels.size() - 1;
        if(levels[depth].find(x) != levels[depth].end())
        {
            if(levels[depth].find(y) != levels[depth].end())
                return levels[depth][x] != levels[depth][y];
            return false;
        }
        return false;
    }
};
