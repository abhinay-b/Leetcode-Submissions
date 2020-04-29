class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        count = 0
        A = list(A)
        for idx in range(len(B)):
            if A[idx] != B[idx]:
                temp = A[idx+1:].index(B[idx])+idx+1
                A[idx], A[temp] = A[temp],A[idx]
                count += 1
        return count
