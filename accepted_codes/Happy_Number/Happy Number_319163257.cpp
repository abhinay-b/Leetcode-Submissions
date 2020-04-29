class Solution {
public:
    bool isHappy(int n) {
        std::unordered_set<int> seen;
        int res;
        while(seen.find(n) == seen.end() && n != 1)
        {
            seen.insert(n);
            res = 0;
            while(n > 0)
            {
                res += (n%10)*(n%10);
                n /= 10;
            }
            n = res;
        }
        return n == 1;
    }
};
