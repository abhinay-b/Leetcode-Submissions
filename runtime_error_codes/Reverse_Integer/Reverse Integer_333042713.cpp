class Solution {
public:
    int reverse(int x) {
        int sign =1,res = 0;
        if(x < 0)
            sign = -1;
        x *= sign;
        while(x>0)
        {
            res *= 10;
            res += x%10;
            x = x/10;
        }
        return sign*res;
    }
};
