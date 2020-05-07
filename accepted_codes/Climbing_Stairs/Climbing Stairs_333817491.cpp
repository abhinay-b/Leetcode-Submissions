class Solution {
public:
    int climbStairs(int n) {
       if(n == 1)
           return 1;
        int curr = 1, prev = 1, count = 1,nxt;
        while(count < n)
        {
            nxt = prev + curr;
            prev = curr;
            curr = nxt;
            count++;
        }
        return curr;
    }
};
