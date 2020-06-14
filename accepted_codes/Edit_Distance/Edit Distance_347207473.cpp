/*
 * Naive: Consider all possibilities and then take minimum among them
 *   minDist(word1, word2) = 1+min(insert,delete,replace)
 *   where insert = minDist(word1, word2.substr(1)),
 *         delete = minDist(word1.substr(1), word2),
 *         replace = minDist(word1.substr(1), word.substr(1))
 * But this will have overlapping substructures. Hence dp
 * Recursive dp: Use the indices of the string to maintain the traversals:
 *               dp[i][j]: minDist to change word1.substr(i) to word2.substr(j)
 *               dp[i][j] = 1+min(insert, delete, replace) if dp[i][j] is not already 
     populated else return dp[i][j]
 * Iterative dp: notice in the above definition that:
 *          insert = dp[i][j+1]
 *          delete = dp[i+1][j]
 *          replace = dp[i+1][j+1]
 * which is a bottom up approach. We can similary see the previous indices to do top down. we 
     will implement top down
*/
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(),n = word2.size();
        int memo[m+1][n+1];
        for(int i = 0; i < m+1; i++)
            memo[i][0] = i;
        for(int j = 0; j < n+1; j++)
            memo[0][j] = j;
        for(int i = 1; i < m+1; i++)
            for(int j = 1; j < n+1; j++)
                if(word1[i-1] == word2[j-1])
                    memo[i][j] = memo[i-1][j-1];
                else
                    memo[i][j] = 1+min(memo[i-1][j-1],min(memo[i][j-1],memo[i-1][j]));
        return memo[m][n];
    }
};
