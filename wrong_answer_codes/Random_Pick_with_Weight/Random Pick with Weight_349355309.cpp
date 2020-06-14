class Solution {
    private:
        vector<int>weights;
        int len;
        
public:
    Solution(vector<int>& w) {
        weights = w;
        len = w.size();
        srand(NULL);
    }
    
    int pickIndex() {
        return ((int)rand())%len;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
