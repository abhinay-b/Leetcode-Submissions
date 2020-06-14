/*
 * Idea: Build a graph and do BFS traversal to reach the destination.
 * BFS queue: store (node,depth,weight) in it.
 * if node on top of queue is dst, update its weight to minimum.
 * Add to queue as long as depth <= K
*/
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        unordered_map<int,vector<pair<int,int>>> adj;
        for(auto &plane : flights)
                adj[plane[0]].push_back(pair(plane[1],plane[2]));
        deque<tuple<int,int,int>>queue;
        queue.push_back(tuple(src,0,0));
        int cost = INT_MAX;
        while(queue.size())
        {
            auto [node,depth,weight] = queue.front();
            queue.pop_front();
            if(node == dst)
                cost = min(cost, weight);
            else if(depth <= K)
            {
                for(auto &nhbr: adj[node])
                    queue.push_back(tuple(nhbr.first,depth+1,weight+nhbr.second));
            }
        }
        if(cost == INT_MAX)
            return -1;
        return cost;
    }
};
