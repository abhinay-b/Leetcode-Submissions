/*
XOR gives the result after adding 2 bits while AND (after left shifting) gives the carry bits.
XOR automatically adds where there is no carry (as only one bit is set).
So all we need to do is XOR the carry bits till they reach zero:
    getSum(a,b) = getSum(a^b,(a&b)<<1), if b > 0; else a
Further, to avoid out of range exception, declare the carry as an unsigned int

*/
class Solution {
public:
    int getSum(int a, int b) {
        unsigned int carry = a&b;
        return ((!b) ? a : getSum(a^b,carry<<1));
    }
};
