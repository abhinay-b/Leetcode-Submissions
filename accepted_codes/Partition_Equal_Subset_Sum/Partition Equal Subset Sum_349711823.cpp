/*
 * To partition successfully, the total sum should be divisible by 2
 * Find the halfSum in the given array:
 *              find(halfSum,nums) = any(find(halfSum - nums[i],nums[:i])), if halfSum > 
     nums[i] for all i in [0,nums.size()]
 * We are checking if we can consider an element and find the (halfSum-element) from the  
     remaining sub array (previous to the element) 
 * This idea is very much like 2sum: Given an element in array, can we find target - element 
     in the remaining subarray
 * The recursive solution tries to find the (target-element) repititively: overlapping 
     substructure. Hence DP!
 * DP solution:
 * dp[i][j] = can we find sum i in subarray upto j elements
 * 2 possibilities: 
 *  1. We already found the sum i in subarray upto j-1 elements
 *  2. We found the sum (i-nums[j]) in subarray upto j-1 elements (if i >= nums[j])
 * i.e
 *      dp[i][j] = dp[i][j-1] || dp[i-nums[j]][j-1] if i >= nums[j]
 * Base condition:
 *      dp[0][j] = true for all j 
 * Finally, dp[halfSum][nums.size()] will tell us whether we can find the halfSum when we 
     consider the whole of the array
*/
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if(sum & 1)
            return false;
        sum >>= 1;
        int m = sum+1, n = nums.size()+1;
        vector<vector<bool>>dp(m,vector<bool>(n,false));
        for(int j = 0; j < n; j++)
            dp[0][j] = true;
        for(int i = 1; i < m; i++)
            for(int j = 1; j < n; j++)
                if(dp[i][j-1] || (i - nums[j-1] >= 0 && dp[i - nums[j-1]][j-1]))
                    dp[i][j] = true;
        return dp[m-1][n-1];            
    }
};
