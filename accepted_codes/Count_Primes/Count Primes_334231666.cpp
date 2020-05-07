// Using Seive of Erosthenes: 
// Maintain a boolean array of size n
// For current index i, Mark all its multiples upto n as false. (starting index of multiples 
    will be i as lower indices will be marked in previous iterations)
class Solution {
public:
    int countPrimes(int n) {
        if(n < 2)
            return 0;
        vector<bool> isPrime(n,true);
        isPrime[0] = isPrime[1] = false;
        for(int i = 2; i*i < n; i++)
        {
          if(!isPrime[i])
                continue;
            for(int j = i; j*i < n; j++)
                isPrime[j*i] = false;
        }
        return count_if(isPrime.begin(),isPrime.end(),[](bool x){return x == true;});      
        
    }
};
