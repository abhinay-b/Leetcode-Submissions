/*
 * We will use a memo where memo[i][j]: number of ways to get sum j using array upto index i
 * Then, memo[i][j] will be number of ways to get sum j using array upto i-1 and number of 
     ways to get sum (j-arr[i]) using array upto index i (i because we are assuming 
     inexhaustible number of coins)
 * i.e
 *          memo[i][j] = memo[i-1][j] + memo[i][j-arr[i]]
 * Boundary case: memo[i][0] = 1 and memo[0][j] = 0 for all j in [1,amount]. Here 0 indicates 
     when there's no array(instd of idx 0)
 * small change to defn: memo[i][j] = number of ways to get sum j using array upto index i-1
 * 
 
 *OPTIMIZATION IN SPACE: We can retain prev row entries and modify using only current row. 
     Hence one row is sufficient,i.e 
 * 1D array: memo[j] += memo[j-arr[i]]
 * initialization: memo[0] = 1, memo[i] = 0, for i in [1,amount] where n = arr.size()
 * return value: memo[amount]
*/
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int>memo(amount+1,0);
        int n = coins.size();
        if(amount == 0)
            return 1;
        if(n == 0)
            return 0;
        memo[0] = 1;
        for(const auto &coin: coins)
        {
            for(int j = coin; j <= amount; j++)
            {
               memo[j] += memo[j-coin];
            }
        }
        return memo[amount];
    }
};
