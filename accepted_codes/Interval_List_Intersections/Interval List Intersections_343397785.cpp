class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<vector<int>>res;
        int lower, upper;
        int i = 0, j = 0;
        while(i < A.size() && j < B.size())
        {
            if(A[i][0] <= B[j][0] && B[j][0] <= A[i][1])
                lower = B[j][0];
            else if(B[j][0] <= A[i][0] && A[i][0] <= B[j][1])
                lower = A[i][0];
            if(A[i][0] <= B[j][1] && B[j][1] <= A[i][1])
            {
                upper = B[j][1];
                j++;
                res.push_back({lower,upper});
            }
            else if(B[j][0] <= A[i][1] && A[i][1] <= B[j][1])
            {
                upper = A[i][1];
                i++;
                res.push_back({lower,upper});
            }            
            else if(A[i][1] <= B[j][1])
                i++;
            else
                j++;
        }
        return res;
    }
};
