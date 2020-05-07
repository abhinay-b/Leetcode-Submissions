class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int len = nums.size();
        for(auto num:nums)
        {
            if(num < 0)
                num *= -1;
            if(num < len)
                nums[num] *= -1;
        }
        
        for(int i = 0; i < nums.size(); i++)
            if(nums[i] > 0)
                return i;
        
        return len;
    }
};
