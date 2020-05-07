class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(auto num:nums)
        {
            if(seen.find(num) == seen.end())
            {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};
