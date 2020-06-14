/*
 * We will generate a graph with an edge between nodes to indicate disliking between the nodes
 * Do a BFS traversal and check if the nhbrs fall in same or different group/set.
 * Maintain a visited set to avoid adding to BFS queue
*/
class Solution {
    void buildGraph(vector<vector<int>>& dislikes, unordered_map<int,vector<int>>&dict)
    {
        for(auto &iter : dislikes)
        {
            dict[iter[0]].push_back(iter[1]);
            dict[iter[1]].push_back(iter[0]);
        }
    }
    bool BFS(int N, unordered_map<int,vector<int>>&dict)
    {
        deque<int>q;
        unordered_set<int> sets[2], visited;
        int num, idx;
        for(int start = 1; start <= N; start++)
        {
            if(visited.find(start) == visited.end())
            {
                q.push_back(start);
                sets[0].insert(start);
                while(q.size())
                {
                    num = q.front();
                    q.pop_front();
                    if(sets[0].find(num) != sets[0].end())
                        idx = 0;
                    else
                        idx = 1;
                    // cout<<num<<":"<<idx<<" ";
                    for(auto &nhbr: dict[num])
                    {
                        if(sets[idx].find(nhbr) != sets[idx].end())
                            return false;
                        // cout<<nhbr<<":"<<idx<<endl;
                        sets[1-idx].insert(nhbr);
                        if(visited.find(nhbr) == visited.end())
                        {
                            visited.insert(nhbr);
                            q.push_back(nhbr);
                        }
                    }
                }
            }
        }
                
        return true;
    }
public:
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        if(dislikes.size() == 0 || dislikes[0].size() == 0)
            return true;
        unordered_map<int,vector<int>>dict;        
        buildGraph(dislikes,dict);
        return BFS(N, dict);
    }
};
