/*
 * We use the following DP idea to solve this problem:
 *  matrix[i][j] can be a square of size k only if all of its predecessors ([i][j-1], [i
     -1][j], [i-1][j-1]) are already of size k-1 and the matrix[i][j] is not a zero
 * The equation which guarantees this is:
            matrix[i][j] += min(matrix[i-1][j-1], min(matrix[i-1][j], matrix[i][j-1])) if 
                matrix[i][j] == 1
*/
class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        if(matrix.size() == 0 || matrix[0].size() == 0)
            return 0;
        int count = 0;
        for(int j = 0; j < matrix[0].size(); j++)
            count += matrix[0][j];
        for(int i = 1; i < matrix.size(); i++)
            count += matrix[i][0];
        for(int i = 1; i < matrix.size(); i++)
            for(int j = 1; j < matrix[0].size(); j++)
            {
                if(matrix[i][j] == 1)
                {
                    matrix[i][j] += min(matrix[i-1][j-1], min(matrix[i-1][j], matrix[i][j-1]
                        ));
                    count += matrix[i][j];
                }
                
            }
        return count;
    }

