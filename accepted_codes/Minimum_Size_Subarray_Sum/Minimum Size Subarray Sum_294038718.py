class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        start = uptoSum = 0
        minSize = len(nums)+1
        for i in range(len(nums)):            
            uptoSum += nums[i]            
            while (uptoSum-nums[start]) > s and start < i:
                uptoSum -= nums[start]
                start += 1
            if (uptoSum-nums[start]) >= s:
                start +=1
                uptoSum -= nums[start]
                minSize = min(minSize,i-start+1)
            elif uptoSum >= s:
                minSize = min(minSize,i-start+1)
                uptoSum -= nums[start]
                start += 1
            if minSize == 1:
                return minSize
        return minSize if minSize < len(nums)+1 else 0
            
            
