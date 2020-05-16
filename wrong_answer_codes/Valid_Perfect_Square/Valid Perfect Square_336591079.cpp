class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num < 0)
            return false;
        unsigned int left = 0, right = num;
        unsigned int mid;
        while(left < right)
        {
            mid = left + (right - left)/2;
            if(mid*mid < num)
                left = mid+1;
            else
                right = mid;
        }
        return left*left == num;            
    }
};
