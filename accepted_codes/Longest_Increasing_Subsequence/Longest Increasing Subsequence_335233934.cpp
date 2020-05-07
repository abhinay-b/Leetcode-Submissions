class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int>subseq(nums.size());
        int maxVal = 0, currMax = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            currMax = 0;
            for(int j = 0; j < i; j++)
            {
                if(nums[j] < nums[i])
                    currMax = max(currMax, subseq[j]);
            }
            subseq[i] = currMax + 1;
            maxVal = max(maxVal, subseq[i]);
        }
        return maxVal;
    }
};
