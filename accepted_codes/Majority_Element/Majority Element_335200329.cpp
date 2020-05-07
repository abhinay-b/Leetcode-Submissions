// The majority element will have majority votes.
// Idea is to consider each number as a candidate and track his count
// whenever the count reaches zero, elect another candidate
// Since the majority element occurs more than n/2 times, it will have positive count by the 
    end
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        int vote = 0;
        int leader = nums[0];
        for(auto num : nums)
        {
            if(num == leader)
                vote++;
            else
                vote--;
            if(vote <= 0)
            {
                vote = 1;
                leader = num;
            }
        }
        return leader;
    }
};
