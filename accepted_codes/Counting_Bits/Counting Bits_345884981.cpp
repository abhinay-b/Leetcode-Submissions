/*
 * Any number can be split into power of 2 + residual
 * so count[number] = 1 + count[number - pow(2,floor(log_2(number)))]
*/
class Solution {
public:
    vector<int> countBits(int num) {
        if(num == 0)
            return {0};
        vector<int>res(num+1);
        res[0] = 0;
        res[1] = 1;
        for(int i = 2; i <= num; i++)
        {
           res[i] = 1 + res[i - pow(2,(int)log2(i))];
        }
        return res;
    }
};
