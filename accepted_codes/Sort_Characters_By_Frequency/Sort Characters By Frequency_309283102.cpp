struct newCompare
{
    bool operator()(pair<int,int> a, pair<int,int> b)
    {
        return a.second < b.second;
    }
};
class Solution {    
public:
    string frequencySort(string s) 
    {
        unordered_map<char,int>dict;
        string res;
        for(int i = 0; i < s.size(); i++)
        {
            dict[s[i]]++;
        }
        
        vector<pair<int,int>>pairs(dict.begin(),dict.end());
        
        sort(pairs.begin(),pairs.end(),[](pair<int,int> a, pair<int,int> b)
        {
            return a.second > b.second;
        });
        
        for(auto const &temp: pairs)
        {
            res += string(temp.second,temp.first);
        }
        return res;
    }
};
