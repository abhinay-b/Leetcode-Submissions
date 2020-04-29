from collections import Counter
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        if not k:
            return True
        
        available = Counter(nums)
        available[0] = 0
        total = sum(nums)
        if total%k:
            return False
        sumVal = int(total/k)
        def helper(nums,current):
            temp = False
            if not nums:
                return False
            for idx,num in enumerate(nums):
                if available[num] and current+num <= sumVal:
                    available[num] -= 1
                    if current+num < sumVal:
                        temp = helper(nums[idx+1:],current+num)
                        if temp:
                            return True
                    else:
                        return True
                    available[num] += 1
            return False
        while available.most_common(1)[0][1] != 0:
            if not helper(nums,0):
                return False
        return True
