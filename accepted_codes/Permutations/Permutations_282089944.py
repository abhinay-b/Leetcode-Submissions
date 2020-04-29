class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def rotateBy1(nums):
            nums = nums[1:]+[nums[0]]
            return nums
        def permutate(tempList,nums):
            if not nums:
                res.append(tempList)
                return
            first = nums[0]
            while True:
                permutate(tempList+[nums[0]],nums[1:])
                nums = rotateBy1(nums)
                if first == nums[0]:
                    break
        res = []
        permutate([],nums)
        return res
