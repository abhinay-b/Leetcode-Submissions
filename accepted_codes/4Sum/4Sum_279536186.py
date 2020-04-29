class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        j = 1
        if len(nums) < 4:
            return res
        while i < len(nums)-3:   
            j = i+1
            while j < len(nums)-2:
                l = j + 1
                r = len(nums)-1
                while l < r:
                    temp = nums[i] + nums[j] + nums[l] + nums[r]
                    if temp == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while(l < r and nums[l] == nums[l+1]):
                            l += 1
                        while(l < r and nums[r] == nums[r-1]):
                            r -= 1
                        l += 1
                        r -= 1
                        continue
                    elif temp < target:
                        while(l < r and nums[l] == nums[l+1]):
                            l += 1
                        l += 1
                    elif temp > target:
                        while(l < r and nums[r] == nums[r-1]):
                            r -= 1
                        r -= 1
                while j < len(nums)-2 and nums[j] == nums[j+1]:
                    j += 1
                j+= 1
            while i < len(nums)-3 and nums[i] == nums[i+1]:
                              i += 1
            i += 1
        return res
