class Solution {
public:
    vector<int>temp;
    vector<vector<int>>res;
    void helper(vector<int>input, int idx, int k)
    {
        if(k == 0)
        {
            res.push_back(temp);
        }
        for(int i = idx; i < input.size(); i++)
        {
            temp.push_back(input[i]);
            helper(input,i+1,k-1);
            temp.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) 
    {
        vector<int>input(n);
        iota(input.begin(),input.end(),1);
        helper(input,0,k);
        return res;
    }
};
