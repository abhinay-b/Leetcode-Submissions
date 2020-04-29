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
        priority_queue<pair<int,int>,vector<pair<int,int>>, newCompare> pQueue;
        pair<int,int> temp;
        for(auto item : dict)
        {
            pQueue.push(item);
        }
        while(!pQueue.empty())
        {
            temp = pQueue.top();
            for(auto i = 0; i < temp.second;i++)
                res += temp.first;
            pQueue.pop();
        }
        return res;
    }
};
