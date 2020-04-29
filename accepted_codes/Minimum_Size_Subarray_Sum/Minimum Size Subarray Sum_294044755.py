class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        start = uptoSum = 0
        minSize = len(nums)+1
        flag = False
        for i in range(len(nums)):            
            uptoSum += nums[i]            
            while (uptoSum > s and start < i):
                flag = True
                uptoSum -= nums[start]
                start += 1
            if uptoSum >= s:
                minSize = min(minSize,i-start+1)
                uptoSum -= nums[start]
                start +=1
            elif flag:
                minSize = min(minSize,i-start+2)
                flag = False            
            if minSize == 1:
                return minSize
        return minSize if minSize < len(nums)+1 else 0
            
            
