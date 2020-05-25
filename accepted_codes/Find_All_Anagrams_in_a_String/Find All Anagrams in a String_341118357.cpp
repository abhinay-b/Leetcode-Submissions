/*
 * Given a target string p of length m, the idea is to check if substring in s and p are 
     anagrams
 * substrings in s to consider: [0,m), [m,2m), .....[n-m,n) where n is the length of s
 * checking anagrams: compare the freq maps of the two strings
*/
class Solution {
    bool checkAnagram(std::unordered_map<char,int>map1, std::unordered_map<char,int>map2)
    {
        for(auto &[key,val] : map2) 
        {
            if(map1[key] != val)
                return false;
        }
        return true;
    }
public:
    vector<int> findAnagrams(string s, string p) {
        std::unordered_map<char,int>freqS,freqP;
        vector<int>res;
        int m =  p.size(), n = s.size();
        for(int i = 0; i < m; i++)
        {
            freqP[p[i]]++;
            freqS[s[i]]++;
        }
        
        for(int i = m; i <= n; i++)
        {
            if(checkAnagram(freqS, freqP))
                res.push_back(i - m);
            freqS[s[i-m]]--;
            if(i < n)
                freqS[s[i]]++;
        }
        return res;
    }
};
