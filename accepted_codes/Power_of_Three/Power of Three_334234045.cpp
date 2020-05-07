class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n <= 0)
            return false;
       int root = ceil(log(n) / log(3));
        return pow(3,root) == n;
    }
};
