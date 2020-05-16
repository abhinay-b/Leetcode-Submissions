class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num < 0)
            return false;
        float left = 0, right = num;
        float mid;
        while(left < right)
        {
            mid = (int) (left + (right - left)/2);
            // cout<<left<<" "<<mid*mid<<" "<<right<<endl;
            if((mid*mid) < num)
                left = mid+1;
            else
                right = mid;
        }
        return left*left == num;            
    }
};
