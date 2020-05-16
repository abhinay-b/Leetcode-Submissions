/*
* Consider the [start,start+k] elements and choose minimum among them. Mark the index of the 
    minimum element.
* Decrement k by index as those elements are equal to being deleted.
* Repeat the above step till k > 0.
* copy the remaining, if any, in the original array to get the result.
* Check for leading zeros in the output and delete it.
*/
class Solution {
public:
    string removeKdigits(string num, int k) {
        if(num.size() == 0 or num.size() == k)
            return "0";
        if(k == 0)
            return num;
        int start = 0,index;
        string res = "";
        while(k > 0)
        {
            index = std::min_element(num.begin()+start, num.begin()+start+k+1) - (num.begin
                ());
            // cout<<start<<" "<<index<<" "<<res.size()<<endl;
            if(index < num.size() && (res.size() != 0 || num[index] != '0'))
                res += num[index];
            k -= (index-start);
            start = index+1;
        }
        
        if(start < num.size())
            res += num.substr(start);
        
        if(res.size() == 0)
            res = "0";
        return res;
    }

