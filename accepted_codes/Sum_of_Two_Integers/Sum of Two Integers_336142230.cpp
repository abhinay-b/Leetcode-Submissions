class Solution {
public:
    int getSum(int a, int b) {
        unsigned int carry = 0;
        while(b)
        {
            carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
};