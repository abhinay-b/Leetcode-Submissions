/*
 * Given a target string p of length m, the idea is to check if substring in s and p are 
     anagrams
 * substrings in s to consider: [0,m), [m,2m), .....[n-m,n) where n is the length of s
 * checking anagrams: compare the freq maps of the two strings
*/
class Solution {
    bool checkAnagram(vector<int>map1, vector<int>map2)
    {
        for(int i = 0; i < map1.size(); i++) 
        {
            if(map1[i] != map2[i])
                return false;
        }
        return true;
    }
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int>freqS(26),freqP(26);
        vector<int>res;
        int m =  p.size(), n = s.size();
        if(n < m)
            return {};
        for(int i = 0; i < m; i++)
        {
            freqP[p[i]-'a']++;
            freqS[s[i]-'a']++;
        }
        
        for(int i = m; i <= n; i++)
        {
            if(checkAnagram(freqS, freqP))
                res.push_back(i - m);
            freqS[s[i-m]-'a']--;
            if(i < n)
                freqS[s[i]-'a']++;
        }
        return res;
    }
};
