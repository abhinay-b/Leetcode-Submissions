/*
 * Understanding the problem statement: An index is picked up based on its weightage. For eg, 
     [1,3] indicates that the 0 index should be picked up 1 in 4 times while index 2 should be 
     picked up 3 in 4 times by the random function.
 * Idea: For randomness, we will use rand function to get a number between 0 to total 
     weightage-1.
 * In the above example, rand will return 0 to 3. We map every occurence of 0 to index 0 while 
     occurence of 1,2,3 to idx 1
 * We achieve such a mapping by maintaining a cumulative weight array and doing a binary 
     search into it.
 * For example, the cumulative array for [1,3] will be [1,4]. if rand returns 2, binary search 
     returns index as 1.
*/
class Solution {
    private:
        vector<int>cumulative;
        int length;
        int binarySearch(int target)
        {
            int left = 0,right = cumulative.size(), mid;
            while(left < right)
            {
               mid = left + (right-left) /2 ;
               if(cumulative[mid] <= target)
                   left = mid+1;
                else
                    right = mid;
            }
            return left;
        }
        
public:
    Solution(vector<int>& w) {
        cumulative = w;
        srand(NULL);
        for(int i = 1; i < w.size();i++)
            cumulative[i] += cumulative[i-1];
        if(w.size() == 0)
            length = 0;
        else
            length = cumulative.back();
    }
    
    int pickIndex() {
        if(!length)
            return -1;
        int target = rand() % length;
        return binarySearch(target);
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
