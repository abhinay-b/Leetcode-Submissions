class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>buff;
        int element;
        for(auto i = 0; i < nums.size() ; i++)
        {
            element = nums[i];
            cout<<element<<endl;
            if(buff.find(target-element) == buff.end())
                buff[element] = i;
            else
                return {i,buff[target-element]};
        }
        return {-1,-1}; //Unnecessary but a good output
    }
};
