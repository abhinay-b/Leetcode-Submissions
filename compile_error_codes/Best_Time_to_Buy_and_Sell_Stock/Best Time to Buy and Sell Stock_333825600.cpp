class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 0)
            return 0;
        int minVal = prices[0];
        int maxProfit = 0;
        for(auto val:prices)
        {
            maxProfit = max(maxProfit, val - minVal);
            minVal = min(minVal, val);
        }
        return maxVal;
    }
};
