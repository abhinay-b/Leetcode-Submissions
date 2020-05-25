/*
 * Idea is to keep track of each character while traversing the input string
 * have a counter map of target string and decrement when there is a match
 * if there is no match, we need to break and start from next index
 * next index is to be determined by the break point character
 * if the character is in target string, search for its first occurence and next index will be 
     the new starting point
 * to search for the first occurence, we will maintain a map of the character and list of its 
     occurences
*/
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        std::unordered_map<char,int> freq,counter;
        std::unordered_map<char,vector<int>> occurs;
        vector<int>res;
        int start = 0, next, ctr;
        int end = s.size() - p.size();
        int j;
        for(auto &iter:p)
            freq[iter]++;
        while(start <= end)
        {
            //Maintain a counter map of target string and decrement when there is a match
            counter = freq;            
            //Maintain a map of the character and list of its occurences
            occurs.clear();
            ctr = 0;
            for(j = start; j < s.size() && j < start+p.size(); j++)
            {
                //Search if there is a match in the target string
                if(counter[s[j]] > 0)
                {
                    counter[s[j]]--;
                    occurs[s[j]].push_back(j);
                    ctr++;
                }
                else
                {
                 // Determine the next starting point for next iteration. This can be a break 
                     point for 2 reasons
                  next = 1;
                 // 1. A character of target that is already exhausted repeats. Search for 
                     this character for its first occurence and select the next index
                  if(occurs.find(s[j]) != occurs.end())
                      next += occurs[s[j]][0]; 
                 //2. The character is not present at all in the target. Make the next index 
                     as starting point
                  else
                      next += j;
                  break;
                }
                
            }
            //if the ctr = target size, add starting point to the result
            // Also, check if the next letter is same as the letter at starting point
            //eg: target: ba, input:abab 
            //starting point is 0. The letter at 0 repeats again at 3. so we can have 1 also 
                as starting point
            //similary, letter at 1 repeats at 4, making 2 a starting point as well
            if(ctr == p.size())
            {
                res.push_back(start);
                while(j < s.size() && s[start] == s[j])
                {
                   res.push_back(start+1);
                   start++;
                   j++;
                }
                start += 2;       
            }
            //if there was a breaking point, choose the next index as the new starting point
            else
                start = next;
        }
        return res;
    }
};
