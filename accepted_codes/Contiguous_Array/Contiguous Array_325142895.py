from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxVal = 0
        dictn = defaultdict(int)
        dictn[0] = -1
        count = 0
        for idx,num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in dictn:
                maxVal = max(maxVal, idx - dictn[count])
            else:
                dictn[count] = idx
        return max(maxVal, dictn[0]+1)         
