/*
 * We will model it as a directed graph problem and use topological sort to check for cycles
 * An edge from src node to dest node implies course at src can only come after course at dest
 * We will maintain a set instead of stack while doing a DFS till we reach the first prereq in 
     the path
 * We will check in the set if the dest node was already a src node to report cycle
*/
class Solution {
    bool helper(int start, unordered_map<int,vector<int>>&dict,unordered_set<int>&visited
        ,unordered_set<int>&stack)
    {
        if(visited.find(start) != visited.end())
            return true;
        if(stack.find(start) != stack.end())
            return false;
        stack.insert(start);
        for(auto &iter: dict[start])
            if(!helper(iter, dict, visited,stack))
                return false;
        stack.erase(start);
        visited.insert(start);
        return true;
    }
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        if(prerequisites.size() == 0 || prerequisites[0].size() == 0)
            return true;
        unordered_map<int,vector<int>>dict;
        for(auto &iter: prerequisites)
        {
            dict[iter[0]].push_back(iter[1]);
        }
        unordered_set<int> visited, stack;
        for(int i = 0; i < numCourses; i++)
            if(!helper(i,dict,visited,stack))
                return false;
        return true;
    }
};
