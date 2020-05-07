// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
//         we will implement binary search to reduce the number of API calls
//         find the mid point in the range. if mid is bad, right = mid. else left = mid
        int left,right,mid;
        left = 1;
        right = n;
        while(left < right)
        {
           mid = left + (right - left) / 2;
            if(isBadVersion(mid))
            {
                right = mid;
            }
            else
                left = mid+1; 
        }
        if(isBadVersion(left))
            return left;
        return -1;
    }
};
