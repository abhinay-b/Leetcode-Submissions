class Solution {
    int dfsUtil( vector<vector<int>> &grid, int x, int y, vector<vector<bool>> &visited )
    {
        if (grid.size() <= x  || grid[0].size() <= y || x < 0 || y < 0  )
            return  INT_MAX;
        if (visited[x][y])
            return grid[x][y];
        visited[x][y] = true;
        if ( grid[x][y] == 0)
            return 0;
        vector<int> adj_distances(4,0);
        adj_distances[0] = dfsUtil(grid, x, y+1, visited);
        adj_distances[1] = dfsUtil(grid, x-1, y, visited);
        adj_distances[2] = dfsUtil(grid, x, y-1, visited);
        adj_distances[3] = dfsUtil(grid, x+1, y , visited);
        return  1 + *(std::min_element(adj_distances.begin(), adj_distances.end())); 
    }

public:
    std::vector<std::vector<int>>updateMatrix(std::vector<std::vector<int>> grid)
    {
        std::vector<std::vector<bool>> visited(grid.size(), vector<bool> (grid[0].size()));
        if (grid.size() == 0)
            return grid;
        if( grid[0].size() == 0)
            return grid;
        int rows = grid.size();
        int cols = grid[0].size();
        for (int i = 0; i < rows; i++)
            for (int j =0; j< cols; j++)
                {
                    grid[i][j] = dfsUtil(grid, i , j,  visited);
                }
    return grid;
}


};
