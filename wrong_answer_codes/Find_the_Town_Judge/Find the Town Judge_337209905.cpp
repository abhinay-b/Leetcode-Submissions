class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        std::unordered_set<int>candidates;
        for(int i = 1; i <= N; i++)
            candidates.insert(i);
        for(auto score: trust)
        {
                candidates.erase(score[0]);
        }
        if(candidates.size() > 0)
            return *(candidates.begin());
        return -1;
    }
};
