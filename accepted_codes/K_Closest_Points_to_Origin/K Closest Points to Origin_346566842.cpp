/*
 * Maintain a max heap of k points. If a new point has lesser distance than the top point, pop 
     and push
 * We will use priority queue with tuple of distance, i, j values
*/
class Solution {
    int euclidDist(vector<int>&p1, vector<int>&p2)
    {
        return pow(p1[0] - p2[0],2)+pow(p1[1]-p2[1],2);
    }
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        if(points.size() <= K || !(points[0].size()))
            return points;
        vector<vector<int>> res;
        vector<int>zero = {0,0};
        int dist1;
        priority_queue<tuple<int,int,int>> heapq;
        for(int i = 0; i < K; i++)
            heapq.push(tuple(euclidDist(zero,points[i]),points[i][0],points[i][1]));
        for(int i = K; i < points.size(); i++)
        {
            auto [dist2, x, y] = heapq.top();
            dist1 = euclidDist(zero,points[i]);
            if(dist2 > dist1)
            {
                heapq.pop();
                heapq.push(tuple(dist1, points[i][0],points[i][1]));
            }
        }
        while(heapq.size())
        {
            auto [dist2, x, y] = heapq.top();
            heapq.pop();
            res.push_back({x,y});
        }
        return res;
    }
};
