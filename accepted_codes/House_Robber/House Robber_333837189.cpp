/*
* consider all possible cases. For eg: [7,2,1,5,3]
* here, stealing from 7,5 gives max amount. so at house 5, we should check which previous 
    houses give best amount
* so at every house we need to maintain the amount upto house-2 as well as upto house-3 and 
    choose max between them.
* i.e amount[i] = house[i] + max(amount[i-2],amount[i-3])
* space optimization: store only 2 values that are needed at any time.
*/
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        if(nums.size() == 1)
            return nums[0];
        vector<int>prev = {nums[0],nums[1]};
        for(int i = 2; i < nums.size();i++)
        {
//             before we update the value, we will store the max between the houses so that we 
    choose the right one for next iteration.
            prev[1-i%2] = max(prev[0],prev[1]);
//             update the value at the corresponding position.
            prev[i%2] += nums[i]; 
        }
        return max(prev[0],prev[1]);
    }
};
