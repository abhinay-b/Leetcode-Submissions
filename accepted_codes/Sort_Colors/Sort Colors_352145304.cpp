/*
 * Maintain a left and right indices. 
 * Left index indicates the first non occurence of red when traversed from left to right
 * Right index indicates the first non occurence of blue when traversed from right to left
 * traverse from left to right and compare the current element. Swap it with left or right 
     accordingly
 * Repeat the above for all elements from left to right
*/
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0, right = nums.size()-1;
        for(int i = left; i <= right;)
        {
            //swap with right index if curr val is 2 and decrement right index
            if(nums[i] == 2)
                swap(nums[i],nums[right--]);
           //Note that left index value will not have value of 2 as it would have been swapped 
               by prev condition
           // Similarly, it will not have 0.
           //So on swapping, i will contain 1 which doesn't need to be swapped. So, we 
               increment i as well.  
            else if(nums[i] == 0)
                swap(nums[left++],nums[i++]); 
            else 
                i++;
        }
    }
};
