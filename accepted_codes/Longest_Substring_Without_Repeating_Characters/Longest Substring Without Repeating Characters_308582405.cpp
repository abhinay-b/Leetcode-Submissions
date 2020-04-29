class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string substr;
        int maxVal = 0,idx;
        for(auto i = 0; i < s.size(); i++)
        {
            idx = substr.find(s[i]);
            if(idx == -1)
            {
                substr += s[i];
            }
            else
            {
                if(substr.size() > maxVal)
                    maxVal = substr.size();
                // cout<<substr<<endl;
                substr = substr.substr(idx+1,substr.size()) + s[i];
                // cout<<substr<<endl;
            }
        }
        if(substr.size() > maxVal)
            maxVal = substr.size();
        return maxVal;
    }
};
