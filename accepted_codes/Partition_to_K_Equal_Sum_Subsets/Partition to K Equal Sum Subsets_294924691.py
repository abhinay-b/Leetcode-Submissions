from collections import Counter
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        if not k or k == 1:
            return True
        total = sum(nums)
        if total%k:
            return False
        target = total / k
        taken = Counter(nums)
        def helper(j,currSum,currIdx,start):
            if j == k:
                return True
            if currIdx == len(nums):
                return False
            idx = currIdx
            while idx < len(nums):
                if taken[nums[idx]]:                
                    temp = currSum+nums[idx]
                    if temp < target:
                        taken[nums[idx]] -= 1
                        if not helper(j,temp,idx+1,start):
                            taken[nums[idx]] += 1
                        else:
                            return True
                    elif temp == target:
                        taken[nums[idx]] -= 1
                        if not helper(j+1,0,start+1,start+1):
                            taken[nums[idx]] += 1
                        else:
                            return True
                idx += 1
            return False
        return helper(0,0,0,0)
