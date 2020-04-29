class Solution {
    vector<int>temp;
    vector<vector<int>>res;
    void helper(vector<int>& nums,int idx, int k)
    {
        if(k == 0)
        {
            res.push_back(temp);
            return;
        }
        for(int i = idx; i < nums.size() ; i++)
        {
            temp.push_back(nums[i]);
            helper(nums,i+1,k-1);
            temp.pop_back();
        }
    }
    
public:
    vector<vector<int>> subsets(vector<int>& nums)
    {
        for(int k = 0; k <= nums.size(); k++)
        {
            helper(nums,0,k);
        }
        return res;

    }
};
