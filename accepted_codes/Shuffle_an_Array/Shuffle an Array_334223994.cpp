/*
* We will choose a random index from the given array of size n. 
* Pick the corresponding number & swap the last element and this number.
* Now we will choose a random index from array of size n-1 (don't consider the last element as 
    it is already picked)
* Continue in this manner to get a shuffled array
*/
class Solution {
private:
    vector<int>original, mixed;
    void swap(int *a, int *b)
    {
        int temp;
        temp = *a;
        *a = *b;
        *b = temp;            
    }
public:
    Solution(vector<int>& nums) {
        original = mixed = nums;
        srand(time(0));
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        mixed = original;
        return mixed;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        int idx, len = original.size();
        for(int i = len-1; i > 0;i--)
        {
          idx = rand() % (i+1);
          swap(&mixed[idx],&mixed[i]);
        }
        return mixed;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
