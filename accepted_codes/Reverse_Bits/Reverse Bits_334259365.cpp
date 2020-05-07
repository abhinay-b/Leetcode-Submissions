class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int power = 31;
        uint32_t res = 0;
        while(n)
        {
            res += pow(2,power--)*(n&1);
            n >>= 1;
        }
        return res;
    }
};
