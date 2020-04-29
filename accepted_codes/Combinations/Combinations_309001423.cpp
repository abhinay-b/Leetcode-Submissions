class Solution {
public:
    void helper(vector<int>input, int idx, int k,  vector<int>temp, vector<vector<int>>*res)
    {
        if(k == 0)
        {
            res->push_back(temp);
        }
        for(int i = idx; i < input.size(); i++)
        {
            temp.push_back(input[i]);
            helper(input,i+1,k-1,temp,res);
            temp.erase(temp.end()-1);
        }
    }
    vector<vector<int>> combine(int n, int k) 
    {
        vector<int>input(n);
        iota(input.begin(),input.end(),1);
        vector<vector<int>>res;
        helper(input,0,k,{},&res);
        return res;
    }
};
