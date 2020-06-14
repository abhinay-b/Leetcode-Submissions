/*
 * Create a vector for each character and store a vector of indices of occurence.
 * Iterate thru the search string s and try to find an ascending order of indices in t using 
     the above vector
*/
class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(s == "")
            return true;
        if(t == "")
            return false;
        vector<vector<int>>indices(26);
        vector<int>res;
        int index,j;
        for(int i = 0; i < t.size(); i++)
            indices[t[i]-'a'].push_back(i);
        for(int i = 0; i < s.size(); i++)
        {
            index = s[i]-'a';
            if(indices[index].size() == 0)
                return false;
            if(res.size() == 0)
                res.push_back(indices[index][0]);
            else
            {
                for(j = 0; j < indices[index].size() && res.back() >= indices[index][j]; j++);
                if(j == indices[index].size())
                    return false;
                res.push_back(indices[index][j]);
            }
        }
        return true;
    }
};
