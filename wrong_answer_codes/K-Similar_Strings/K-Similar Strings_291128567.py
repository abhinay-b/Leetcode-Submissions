class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        dictn = dict()
        count = 0
        for idx,char in enumerate(A):
            dictn[char] = idx
        for idx in range(len(B)):
            if idx != dictn[B[idx]]:
                dictn[A[idx]],dictn[B[idx]] = dictn[B[idx]],dictn[A[idx]]
                count += 1
        return count
