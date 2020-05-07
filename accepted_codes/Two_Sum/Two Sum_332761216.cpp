class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>buff;
        int element;
        for(auto i = 0; i < nums.size() ; i++)
        {
            element = nums[i];
            if(buff.find(target-element) != buff.end())
                return {i,buff[target-element]};
            buff[element] = i;
        }
        return {};
    }
};
