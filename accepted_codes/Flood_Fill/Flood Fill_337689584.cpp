class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        std::deque<pair<int,int>> queue;
        if(image.size() == 0 || image[0].size() == 0)
            return image;
        int rows = image.size(), cols = image[0].size();
        vector<vector<int>> nhbrs;
        int oldColor = image[sr][sc];
        image[sr][sc] = -1;
        queue.push_back(pair(sr,sc));
        while(queue.size())
        {
            auto [cr, cc] = queue.front();
            queue.pop_front();
            nhbrs = {{cr+1,cc},{cr-1,cc},{cr,cc-1},{cr,cc+1}};
            for(auto nhbr:nhbrs)
            {
                if(0<= nhbr[0] && nhbr[0] < rows && 0 <= nhbr[1] && nhbr[1] < cols && 
                    image[nhbr[0]][nhbr[1]] == oldColor)
                {
                    image[nhbr[0]][nhbr[1]] = -1;
                    queue.push_back(pair(nhbr[0],nhbr[1]));                    
                }
            }
        }
        for(int i = 0; i < rows; i++)
            for(int j = 0; j < cols; j++)
                if(image[i][j] == -1)
                    image[i][j] = newColor;
        return image;
        
    }
};
