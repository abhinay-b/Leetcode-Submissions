/*
 * Let us count the number of 0s and number of 1s in the stream by adding -1 and 1 each time 
     respectively.
 * If a count repeats itself after few steps in the stream, this mean that we added opposite 
     values to balance out.
 * eg:     [0,1,1,0]
 * counts: [-1,0,1,0] (Clearly 0 repeats again as there was a 0 opposing the count of 1 
     balancing out number of 0s and 1s.)
 * We will maintain a dictionary of count and its first occurence as the value.
 * whenever a count repeats, we check the length between currenct index and its first 
     occurence. Update max if needed.
 * Also note that the count is zero without considering the array. Hence, we store the first 
     occurence of 0 as -1. 
*/
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        //maintain a dictionary of count and its first occurence as the value.
        std::unordered_map<int,int>dict;
        //The count is 0 without considering the array. Hence, we store the first occurence of 
            0 as -1
        dict[0] = -1;
        int count = 0;
        int maxLen = 0;
        for(int i = 0; i < nums.size();i++)
        {
            //count the number of 0s and number of 1s in the stream by adding -1 and 1 each 
                time respectively.
            count += (nums[i] == 0) ? -1 : 1;
            //whenever a count repeats, we check the length between currenct index and its 
                first occurence.
            if(dict.find(count) != dict.end())
                maxLen = max(maxLen, i - dict[count]);
            else
                dict[count] = i;
        }
        return(maxLen);
    }
};
