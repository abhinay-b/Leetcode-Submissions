class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0: # once we reach positive nums, we can never make a zero sum
                break
            if i > 0 and nums[i] == nums[i-1]: # avoid duplicates
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                curr = nums[l] + nums[r]
                if curr == -nums[i]:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -=1
                elif curr > -nums[i]:
                    r -=1
                else:
                    l += 1
        return ans
