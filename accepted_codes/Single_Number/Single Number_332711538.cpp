class Solution {
public:
    int singleNumber(vector<int>& nums) {
        auto xorIt = [](int num1, int num2)
        {
            return num1 ^ num2;
        };
        return std::accumulate(nums.begin(),nums.end(),0,xorIt);
    }
};
