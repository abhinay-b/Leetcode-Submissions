/*
 * Find the first break point
 * Find the sum after the break point
 * If there are no more break points, add the sum before the break point and after the 
     breakpoint
 * 
*/
class Solution {
    int kadane(vector<int> a) {
        int sum = 0;
        int maxSum = 0;
        int firstIndex = -1;

        for (int i = 0; i < a.size(); i++) {
            sum += a[i];
            if (sum < 0) {
                sum = 0;
            } else {
                maxSum = max(sum, maxSum);
                if (firstIndex == -1)
                    firstIndex = i;
            }
        }
        // starting again from 0 till firstIndex.
        for (int i = 0; i < firstIndex; i++) {
            sum += a[i];
            if (sum < 0) {
                sum = 0;
            } else {
                maxSum = max(sum, maxSum);
            }
        }
        return maxSum;
    }
public:
    int maxSubarraySumCircular(vector<int>& A) {
        int min = INT_MIN;
        bool positive = false;
        for (int i = 0; i < A.size(); i++) {
            if (A[i] >= 0) {
                positive = true;
                break;
            } else {
                if (A[i] > min) {
                    min = A[i];
                }
            }
        }
        if (!positive) {
            return min;
        }
        for (int i = 0; i < A.size(); i++) {
            A[i] = -A[i];
        }

        // run Kadane's algorithm on modified array
        int negMaxSum = kadane(A);

        // restore the array
        for (int i = 0; i < A.size(); i++) {
            A[i] = -A[i];
        }

      /*  return maximum of

         1. sum returned by Kadane's algorithm on original array.

         2. sum returned by Kadane's algorithm on modified array +
            sum of all elements of the array.
         You might be wondering that why we are adding the min sum to total sum. The reason is 
             that the min sum that we have is positive. That's why we are adding it.
      */

        return max(kadane(A), accumulate(A.begin(),A.end(),0) + negMaxSum);
    }
};
