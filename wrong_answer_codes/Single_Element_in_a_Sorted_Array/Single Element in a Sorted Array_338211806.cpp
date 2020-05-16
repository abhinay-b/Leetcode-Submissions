/*
 * Idea: Binary search: Chech the size across mid element:
 * if [left,mid] array is odd and the mid element is same as mid-1 element, then the odd 
     length is cz of the odd element.
 *          shift the left to mid+1
 * if [left,mid] array is even but the mid element is same as mid+1 element, then the even 
     length is cz of the odd element
 *          shift the left to mid+2 (as mid+1 can't be the odd element)
 * else shift the right to mid
*/
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int left = 0, right = nums.size()-1;
        int mid;
        while(left < right)
        {
            mid = left + (right - left)/2;
            if(((!(mid-left+1) % 2) && nums[mid] == nums[mid-1]))
                left = mid+1;
            else if((((mid-left+1)%2) && nums[mid] == nums[mid+1]))
                left = mid+2;
            else
                right = mid;
        }
        return nums[left];
    }
};
