/*
 * Idea is to look at diff = costs[i][0] - costs[i][1]
 * sort it in ascending order and choose the first N for A
 * Maintain a map of diff,idx to get back the values after sorting
 * Time complexity: 2Nlog2N (sorting takes most time)
*/
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        vector<int> diff;
        int res = 0, temp;
        unordered_map<int,vector<int>>findIdx;
        for(int i = 0; i < costs.size(); i++)
        {
            temp = costs[i][0]-costs[i][1];
            diff.push_back(temp);
            findIdx[temp].push_back(i);
        }
        sort(diff.begin(), diff.end());        
        for(int i = 0; i < diff.size()/2; i++)
        {
            temp = findIdx[diff[i]].back();
            findIdx[diff[i]].pop_back();
            res += costs[temp][0];
        }
        for(int i = diff.size()/2; i < diff.size(); i++)
        {
            temp = findIdx[diff[i]].back();
            findIdx[diff[i]].pop_back();
            res += costs[temp][1];
        }
        return res;
    }
};
