class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        res = 0

        if len(nums) < 3:
            return res
        res = nums[0] + nums[1] + nums[2]
        minDiff = target - res
        while i < len(nums)-1:
            l = i+1
            r = len(nums) - 1
            while(l < r):
                temp = nums[i] + nums[l] + nums[r]
                diff = target - temp
                if abs(diff) < abs(minDiff):
                    res = temp
                    # print(temp,diff,minDiff)
                    minDiff = diff

                if diff == 0:
                    return temp
                elif diff > 0:
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                else:
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1


            while i < len(nums) -1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res
