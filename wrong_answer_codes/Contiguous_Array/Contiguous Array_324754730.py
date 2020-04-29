class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = [0]*2
        start = end = 0
        maxVal = -float('inf')
        for idx,num in enumerate(nums):
            count[num] += 1
            diff = abs(count[0] - count[1])
            if diff > 1:
                count[nums[start]] -= 1
                start += 1
            elif diff == 1 and start > 0 and (count[nums[start-1]] + 1 == count[1-nums[start
                -1]]):
                start -= 1
                end = idx
                maxVal = max(maxVal, end - start+1)
            elif not diff:
                end = idx
                maxVal = max(maxVal, end - start+1)
        return maxVal         
