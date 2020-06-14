/*
 * Idea: O(N^2) Solution: for every num, check if num2 < num1 divides num1 and add it to its 
     list. Return largest list
 * Sort the given vector as its complexity is lesser than over all complexity
 * To reduce space complexity, instead of storing the whole list, we can point to the index of 
     the divisor with most number of divisors
 * For this purpose, we need to have 2 vectors: count & indices where
 * count[i]: the count of divisors that the ith element in the given array has
 * indices[i]: the index of the divisor that has the most divisors
*/
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        if(n < 2)
            return nums;
        vector<int>count(n, 1), indices(n, -1);
        int maxIdx = 0;
        sort(nums.begin(),nums.end());
        for(int i = 1; i < n; i++)
        {
            for(int j = 0; j < i; j++)
            {
                if(nums[i] % nums[j] == 0)
                {
                    if(count[i] < count[j]+1)
                    {
                        count[i] = count[j]+1;
                        indices[i] = j;                        
                    }
                }
            }
            if(count[maxIdx] < count[i])            
                maxIdx = i;            
        }
        int idx = maxIdx;
        vector<int>res;
        while(idx >= 0)
        {
            res.push_back(nums[idx]);
            idx = indices[idx];
        }
        // reverse(res.begin(), res.end());
        return res;
    }
};
