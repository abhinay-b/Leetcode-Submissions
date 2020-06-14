class Solution {
    void helper(vector<int>& nums, int idx, vector<int>& temp, set<vector<int>> &res)
    {
        if(idx == nums.size())
            return;
        for(int i = idx; i < nums.size();i++)
        {
            if(temp.size() == 0 || nums[i] >= temp[temp.size()-1])
            {
                temp.push_back(nums[i]);
                 if(temp.size() >1)
                    res.insert(temp);
                helper(nums,i+1,temp, res);
                temp.pop_back();
            }
        }
    }
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        int idx = 0;
        int k = 3;
        vector<int>temp;
        set<vector<int>>res;
        vector<vector<int>>result;
        helper(nums,idx,temp,res);
        for(auto &iter: res)
            result.push_back(iter);
        return result;
    }
};
