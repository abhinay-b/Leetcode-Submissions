from collections import defaultdict
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        count = 0
        mismatch=set()
        minVal = 0
        dictn = defaultdict(set)
        for idx in range(len(A)):
            dictn[A[idx]].add(idx)
            if A[idx] != B[idx]:
                mismatch.add(idx)
        while True:
            if len(mismatch) == 0:
                return minVal
            if len(mismatch) == 2:
                return minVal + 1            
            idx2 = -1
            for i in mismatch:
                for j in mismatch:
                    if i != j and A[i] == B[j] and A[j] == B[i]:
                        idx2 = j
                        break
                if idx2 != -1:
                    break
            # print(i,idx2,mismatch)
            if idx2 != -1:
                mismatch.remove(i)
                mismatch.remove(idx2)
                minVal += 1
            else:
                return minVal + len(mismatch)-1
                        
