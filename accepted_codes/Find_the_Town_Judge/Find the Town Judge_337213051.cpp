class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        std::unordered_set<int>candidates;
        std::unordered_map<int,int>trusted;
        for(int i = 1; i <= N; i++)
            candidates.insert(i);
        for(auto score: trust)
        {
            candidates.erase(score[0]);
            trusted[score[1]]++;
        }
        if(candidates.size() > 0 && trusted[*(candidates.begin())] == N-1)
                return *(candidates.begin());
        return -1;
    }
};
