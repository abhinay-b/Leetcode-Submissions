class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] > 0:
                break       
            l = i+1
            r = len(nums) - 1
            while(l < r):
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    res.append([nums[i],nums[l], nums[r]])
                    l += 1
                    r -= 1
                    continue
                elif temp > 0:
                    r -= 1
                else:
                    l += 1
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
            while i < len(nums) -1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res

