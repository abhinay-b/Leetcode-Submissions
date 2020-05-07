class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int right1 = m-1,right2 = n-1;
        int ptr = m+n-1;
        while(right1>= 0 && right2 >= 0)
        {
            if(nums1[right1] > nums2[right2])
                nums1[ptr] = nums1[right1--];
            else
                nums1[ptr] = nums2[right2--];
            ptr--;
        }
        while(right1 >= 0)
            nums1[ptr--] = nums1[right1--];
        while(right2 >= 0)
            nums1[ptr--] = nums2[right2--];
    }
};
