class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        std::unordered_map<char,int>freq;
        for(int i = 0; i < magazine.size();i++)
            freq[magazine[i]]++;
        int count = 0;
        for(int i = 0; i < ransomNote.size();i++)
            if(freq[ransomNote[i]] != 0)
            {
               freq[ransomNote[i]]--; 
            }
            else
                return false;
        return true;
    }
};
