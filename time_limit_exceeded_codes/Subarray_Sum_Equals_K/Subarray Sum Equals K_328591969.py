from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        dictn = defaultdict(int)
        total = 0
        for idx,num in enumerate(nums):
            total += num
            dictn[idx] = total
        count = 0
        for i in range(len(nums)):
            if dictn[i] == k:
                count += 1
            for j in range(i+1,len(nums)):
                if dictn[j] - dictn[i] == k:
                    count+=1
        return count
