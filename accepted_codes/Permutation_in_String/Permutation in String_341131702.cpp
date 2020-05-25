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
    bool checkInclusion(string p, string s) {
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
                return true;
            freqS[s[i-m]-'a']--;
            if(i < n)
                freqS[s[i]-'a']++;
        }
        return false;
    }
};
