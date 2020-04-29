class Solution {
    int dx[4] = {-1,0,1,0};
    int dy[4] = {0,-1,0,1};
   
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) 
    {
        int rows = matrix.size();
        int cols = matrix[0].size();
        vector<vector<int>>dist(rows,vector<int>(cols,INT_MAX));
        int m,n,p,q;
        pair<int,int> curr;
        deque<pair<int,int>>queue;        
        for(int i = 0; i < rows;i++)
            for(int j = 0; j < cols;j++)
            {
                if(matrix[i][j] == 0)
                {
                    dist[i][j] = 0;
                    queue.push_back(pair(i,j));
                }
            }            
                    
        while(queue.size())
        {
            curr = queue.back();
            queue.pop_back();
            m = curr.first;
            n = curr.second;
            for(int k = 0; k < 4; k++)
            {
                p = m+dx[k];
                q = n+dy[k];             
                if (0 <= p && p < rows && 0 <= q && q < cols && (dist[p][q] > dist[m][n]))
                {
                    dist[p][q] = 1+dist[m][n];
                    queue.push_back(pair(p,q));
                }
            }
        }
        return dist;    
    }
};
