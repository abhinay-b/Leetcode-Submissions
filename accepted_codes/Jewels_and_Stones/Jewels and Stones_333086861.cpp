class Solution {
public:
    int numJewelsInStones(string J, string S) {
        std::unordered_map<char,int>freq;
        for(int i = 0; i < S.size();i++)
            freq[S[i]]++;
        int count = 0;
        for(int i = 0; i < J.size();i++)
            count += freq[J[i]];
        return count;
    }
};
