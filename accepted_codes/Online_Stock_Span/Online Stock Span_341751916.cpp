/*
 * Greedy solution: 
 * Keep track of number of spans of each element in an array, say, span
 * For A[i], if A[i - 1] < A[i]: count = span[i-1]. Atleast count number of elements are less 
     than A[i]
 * directly jump back to i - count and repeat the above process as long as i-count >= 0
*/
class StockSpanner {
    vector<int> elems;
    vector<int>span;
public:
    StockSpanner() {
      
    }
    
    int next(int price) {
        int i = elems.size();
        elems.push_back(price);
        int count = 1;
        int skip = i - 1;
        while(skip >= 0)
        {
            if(elems[i] < elems[skip])
                break;                
            else
            {
                count += span[skip];
                skip -= span[skip];
            }
        }
        span.push_back(count);
        return count;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
