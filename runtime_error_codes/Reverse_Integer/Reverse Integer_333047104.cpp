class Solution {
public:
    int reverse(int x) {
        int sign =1;
        long int res = 0;
        int min = -1*pow(2,31), max = pow(2,31)-1;
        if(x < 0)
            sign = -1;
        x *= sign;
        while(x>0)
        {            
            res *= 10;
            res += x%10;
            x = x/10;
        }
        res *= sign;
        if(min <= res && res <= max)
            return res;
        return 0;
    }
};
