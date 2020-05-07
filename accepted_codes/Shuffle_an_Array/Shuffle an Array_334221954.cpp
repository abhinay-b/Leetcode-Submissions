class Solution {
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
        original.assign(nums.begin(),nums.end());
        mixed.assign(nums.begin(),nums.end());
        srand(time(0));
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        mixed.assign(original.begin(),original.end());
        return mixed;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        int idx, len = original.size();
        for(int i = 0; i < original.size();i++)
        {
          idx = (rand()% (len-i)) +i;
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
