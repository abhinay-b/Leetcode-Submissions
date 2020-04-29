class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string substr;
        int maxVal = 0;
        for(auto i = 0; i < s.size(); i++)
        {
            if(substr.find(s[i]) == -1)
            {
                substr += s[i];
            }
            else
            {
                if(substr.size() > maxVal)
                    maxVal = substr.size();
                substr = "";
            }
        }
        return maxVal;
    }
};
