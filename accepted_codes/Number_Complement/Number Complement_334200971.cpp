class Solution {
public:
    int findComplement(int num) {
        vector<int>res;
        int flip = 0;
        while(num > 0)
        {
            res.push_back(num&1);
            num >>= 1;
        }
        for(int i = 0; i < res.size(); i++)
            flip += pow(2,i) * (1-res[i]);
        return flip;
    }
};
