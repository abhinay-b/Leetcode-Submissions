class Solution {
public:
    int firstUniqChar(string s) {
        std::unordered_map<int,int>freq;
        for(int i = 0; i < s.size(); i++)
            freq[s[i]]++;
        for(int i = 0;i < s.size(); i++)
            if(freq[s[i]] == 1)
                return i;
        return -1;
    }
};
