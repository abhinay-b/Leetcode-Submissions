/*
 * Maintain a string and grow it as long as no repeating characters
 * If there is a repeating character, update max and trim till the occurrence of the character 
     in the string.
 * concatenate the new character to the string
*/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string temp = "";
        int maxVal = 0;
        int idx = 0;
        for(auto &ch : s)
        {
            idx = temp.find(ch);
            if(idx == string::npos)
                temp += ch;
            else
            {
                maxVal = max(maxVal, (int)temp.size());
                temp = temp.substr(idx+1) + ch;
            }
        }
        return max(maxVal, (int)temp.size());
    }
};
