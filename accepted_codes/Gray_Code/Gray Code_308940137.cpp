class Solution {
public:
    vector<int> grayCode(int n) 
    {
        vector<int>res = {0};
        vector<int>temp;
        int highBit = 1;
        for(int i = 0; i < n; i++)
        {
            temp.clear();
            for(int i = res.size()-1; i >= 0; i--)
            {
                temp.push_back(highBit+res[i]);
            }
            highBit <<= 1;
            res.insert(res.end(),temp.begin(),temp.end());
        }
        return res;
    }
};
