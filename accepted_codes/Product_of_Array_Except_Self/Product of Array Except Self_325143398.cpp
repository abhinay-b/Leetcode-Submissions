class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums)
    {
        vector<int>output;
        output.push_back(1);
        int right = 1;
        for(auto i = 1; i < nums.size(); i++)
        {
            output.push_back(nums[i-1]*output[i-1]);
        }
        for(int i = nums.size()-2; i >= 0; i--)
        {
            right *= nums[i+1];
            output[i] *= right;
        }
        return output;
    }
};
