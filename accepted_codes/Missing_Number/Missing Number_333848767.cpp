class Solution {
public:
    int missingNumber(vector<int>& nums) {
//         since it contains from first n natural numbers, we will xor out all the numbers 
    with their indices.
//         using the commutative propery of xor: a^b^c = a^c^b, every (index) must cancel out 
    a natural number (and the 
//         max possible number is n, we will start with n to cancel it out) leaving only one 
    mismatched number.
        int res = nums.size();
        for(int i = 0; i < nums.size(); i++)
            res ^= nums[i] ^ i;
        return res;
    }
};
