from collections import deque
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        count = 0
        A = list(A)
        queue = deque([(A,0,0)])
        minVal = float('inf')
        while queue:
            curr,idx,height = queue.pop()
            while idx < len(curr) and curr[idx] == B[idx]:
                idx += 1
            if idx == len(curr):
                minVal = min(minVal,height)
            else:
                mismatch = idx
                while idx < len(curr):
                    while idx < len(curr) and (curr[idx] == B[idx] or curr[idx] != B[mismatch]
                        ):
                        idx += 1
                    if idx < len(curr):
                        temp = curr.copy()
                        temp[mismatch],temp[idx] = temp[idx],temp[mismatch]
                        queue.appendleft((temp,mismatch+1,height+1))
                        idx += 1
        return minVal
