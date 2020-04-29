from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        dictn = defaultdict(int)
        total = 0        
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            if total == k:
                count += 1
            elif total - k in dictn:
                count += dictn[total-k]
            dictn[total] += 1
        return count
