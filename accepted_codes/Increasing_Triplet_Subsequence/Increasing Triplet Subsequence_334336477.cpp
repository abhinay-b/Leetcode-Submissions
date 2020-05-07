/*
* Idea is to check if at any index in the array, if there is a minval to its left and maxval 
    to its right
* to find the min val, we will check if the minVal upto this point is less than arr[idx]. 
* Yes: arr[idx] has a lower val to its left. No: it doesn't have and it is the minVal now
* apply similar logic for maxVal as well.
* finally check any index has both lower and upper set to true.
*/
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int n = nums.size(), minVal,maxVal;
        if(n < 3)
            return false;
        bool lower[n], upper[n];
        lower[0] = upper[n-1] = false;
        minVal = nums[0];
        for(int i = 1; i < n; i++)
        {
            if(nums[i] <= minVal)
            {
                lower[i] = false;
                minVal = nums[i];
            }
            else
                lower[i] = true;
        }
        
        maxVal = nums[n-1];
        for(int i = n-2; i >= 0; i--)
        {
          if(nums[i] >= maxVal)
          {
              upper[i] = false;
              maxVal = nums[i];
          }
          else
            upper[i] = true;
        }
        
        for(int i = 1; i < n-1; i++)
        {
            // cout<<lower[i] << " "<<upper[i]<<endl;
            if(lower[i] && upper[i])
                return true;
        }
            
        return false;
    }
}; 
