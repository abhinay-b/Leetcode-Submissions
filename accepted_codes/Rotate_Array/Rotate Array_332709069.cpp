class Solution {
public:
    void reverse(vector<int>&nums,int start, int end)
    {
        int temp;
        while(start < end)
        {
            temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
    void rotate(vector<int>& nums, int k) {
//         reverse the subarray from 0 to length - k-1 & the subarray from length-k to the end
//         finally reverse the whole array
        int length = nums.size();
        while(k >= length)
            k -= length;
        reverse(nums,0,length-k-1);
        reverse(nums,length-k,length-1);
        reverse(nums,0,length-1);
    }
};
