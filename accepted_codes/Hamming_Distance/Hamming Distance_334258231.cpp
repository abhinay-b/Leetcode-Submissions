class Solution {
public:
    int hammingDistance(int x, int y) {
        int z = x ^ y, count = 0;
        while(z)
        {
            count += z&1;
            z >>= 1;
        }
        return count;
    }
};
