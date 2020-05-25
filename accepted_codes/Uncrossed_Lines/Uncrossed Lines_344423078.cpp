/*
 * We will use dynamic programming to solve this problem. We will use a memo of mxn size 
     where:
 * memo[i][j] represents the max lines with A[i],A[i+1],.... and B[j],B[j+1],.....
 * We will build this memo bottom up. The last row and the last column are first populated 
     with 1 if there is a match, else 0.
 * For the rest of the memo, we use:
 * if A(i) == B[j]:
 *      memo[i][j] = max(1 + memo[i+1][j+1],  (ie. max crossing without considering current 
     A[i], B[j]) memo[i+1][j],memo[i][j+1])
 * else:
 *      memo[i][j] = max(memo[i+1][j+1], memo[i+1][j], memo[i][j+1])
*/
class Solution {
public:
    int maxUncrossedLines(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size();
        if(!m || !n)
            return 0;
        int memo[m][n];
        memo[m-1][n-1] = 0;
        if(A[m-1] == B[n-1])
            memo[m-1][n-1] = 1;
        //last row
        for(int j = n-2; j >=0; j--)
            if(A[m-1] == B[j])
                memo[m-1][j] = 1;
            else
                memo[m-1][j] = memo[m-1][j+1];
        //last column
        for(int i = m-2; i >= 0; i--)
            if(A[i] == B[n-1])
                memo[i][n-1] = 1;
            else
                memo[i][n-1] = memo[i+1][n-1];
        //rest
        for(int i = m-2; i >= 0; i--)
            for(int j = n-2; j >= 0; j--)
                if(A[i] == B[j])
                    memo[i][j] =max(1+memo[i+1][j+1],max(memo[i+1][j],memo[i][j+1]));
                else
                    memo[i][j] = max(memo[i+1][j+1],max(memo[i+1][j],memo[i][j+1]));
        // for(int i = 0; i < m; i++){
        //     for(int j = 0; j < n; j++)
        //         cout<<memo[i][j]<<" ";
        //     cout<<endl;
        // }
        return memo[0][0];
                
    }

