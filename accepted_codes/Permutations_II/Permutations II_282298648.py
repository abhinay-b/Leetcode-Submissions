class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def rotateByk(nums,k):
            nums = nums[k:]+nums[:k]
            return nums
        def permutate(tempList,nums):
            if not nums:
                res.append(tempList)
                return
            i = 0
            while i < (len(nums)):
                permutate(tempList+[nums[0]],nums[1:])
                j = 0
                while j < len(nums)-1 and nums[j] == nums[j+1]:
                    j += 1
                i += j+1
                nums = rotateByk(nums,j+1)
                # print(nums)
        res = []
        if not nums:
            return res
        nums.sort()
        permutate([],nums)
        return res  
