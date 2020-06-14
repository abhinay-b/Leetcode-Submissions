/*
 * We will maintain a set of available indices and assign the nth available index to the next 
     person of height n
 * To pick the next person, we will maintain a min priority queue, ordered on person's height 
     (and max priority on person's number of people before him)
 * Continue this process till all the people are assigned.
*/
class Comparator{
  public:
    int operator()(const vector<int>&A, const vector<int>&B)
    {
        if(A[0] > B[0])
            return true;
        if(A[0] == B[0] && A[1] < B[1])
            return true;
        return false;
    }
};
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        int n = people.size();
        set<int>indices;
        vector<vector<int>>res(n);
        if(!n || people[0].size() == 0)
            return res;
        priority_queue<vector<int>, vector<vector<int>>,Comparator>pqueue;
        for(int i = 0; i < n; i++)
        {
            indices.insert(i);
            pqueue.push(people[i]);
        }
        vector<int>curr;
        int idx;
        while(pqueue.size())
        {
            curr = pqueue.top();
            pqueue.pop();
            idx = curr[1];
            auto iter = std::next(indices.begin(),idx);
            res[*iter] = curr;
            indices.erase(*iter);
        }
        return res;
        
    }
};
