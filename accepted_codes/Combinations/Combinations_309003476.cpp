class Solution {
    vector<int>temp;
    vector<vector<int>>res;
    void helper(int idx,int n, int k)
    {
        if(k == 0)
        {
            res.push_back(temp);
        }
        for(int i = idx; i <= n ; i++)
        {
            temp.push_back(i);
            helper(i+1,n,k-1);
            temp.pop_back();
        }
    }
public:
    
    vector<vector<int>> combine(int n, int k) 
    {
        vector<int>input(n);
        // iota(input.begin(),input.end(),1);
        helper(1, n, k);
        return res;
    }
};
