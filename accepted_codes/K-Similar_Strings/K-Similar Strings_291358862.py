from collections import deque
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        count = 0
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
                        temp = curr[:mismatch] + curr[idx] +curr[mismatch+1:idx] + 
                            curr[mismatch] + curr[idx+1:]
                        queue.appendleft((temp,mismatch+1,height+1))
                        idx += 1
        return minVal
