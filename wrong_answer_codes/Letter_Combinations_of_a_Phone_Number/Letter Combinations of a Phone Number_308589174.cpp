class Solution {
public:
    void build(string res, string digits, int index, unordered_map<char,vector<char>>smap, 
        vector<string>*output)
    {
        if(index == digits.size())
        {
            output->push_back(res);
        }
        for(auto ltr : smap[digits[index]])
        {
            build(res+ltr,digits,index+1,smap,output);
        }
    }
    vector<string> letterCombinations(string digits) {
        unordered_map<char,vector<char>>smap;
        smap['2'] = {'a','b','c'};
        smap['3'] = {'d','e','f'};
        smap['4'] = {'g','h','i'};
        smap['5'] = {'j', 'k', 'l'};
        smap['6'] = {'m', 'n', 'o'};
        smap['7'] = {'p', 'q', 'r', 's'};
        smap['8'] = {'t', 'u', 'v'};
        smap['9'] = {'w', 'x', 'y', 'z'};
        vector<string>output;
        build("",digits,0,smap,&output);
        return output;
    }
};
