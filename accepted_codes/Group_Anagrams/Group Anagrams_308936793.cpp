class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs)
    {
        unordered_map<string,vector<string>> dict;
        string temp;
        for(auto str:strs)
        {
            temp = str;
            sort(temp.begin(),temp.end());
            dict[temp].push_back(str);
        }
        vector<vector<string>> result;
        for(auto [key,val] : dict)
            result.push_back(val);
        return result;
    }
};
