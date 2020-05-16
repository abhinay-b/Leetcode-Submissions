class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if(coordinates.size() == 2)
            return true;
        
        auto p1 = coordinates[0], p2 = coordinates[1];
        float slope, curr;
        if(p1[0] || p2[0])
            slope = (p2[1] - p1[1]) / (p2[0] - p1[0]);
        else
            slope = FLT_MAX;
        for(int i = 2; i < coordinates.size(); i++)
        {
            p2 = coordinates[i];
            // cout<<p2[0]<<" "<<p2[1]<<" "<<p1[0]<<" "<<p1[1]<<endl;
            if(p1[0] || p2[0])
                curr = (float)(p2[1] - p1[1]) / (p2[0] - p1[0]);
            else
                curr = FLT_MAX;
            // cout<<curr<<" "<<slope<<endl;
            if(curr != slope)
                return false;
        }
        return true;
    }
};
