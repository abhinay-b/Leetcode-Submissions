class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int idx = std::upper_bound(nums.begin(),nums.end(),target)-nums.begin();
        if(idx and nums[idx-1] == target)
            idx--;
        return idx;
    }
};
