class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
//         we will store the larger of the two arrays in a frequency map
//         we will check if every element of smaller array is present in the frequency map
        std::unordered_map<int,int>freq;
        int len1 = nums1.size(),len2=nums2.size();
        vector<int>res;
//         let nums1 be smaller of the arrays. (swap if required)
        if(len2 < len1)
        {
            auto temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
//         Build the frequency map of nums2, the larger of the arrays
        for(auto num:nums2)
        {
            freq[num]++;
        }
        // for(auto [key,val]:freq)
        // {
        //     cout<<key<<" "<<val<<endl;
        // }
//         for each of the number in nums1, check if present in freq map. Decrement if present 
    and add num to result.
        for(auto num:nums1)
        {
            if(freq.find(num) != freq.end() && (freq[num] > 0))
            {
                freq[num]--;
                res.push_back(num);
            }
        }
        return res;
    }
};
