class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        res = []
        for idx in range(len(nums)):
            travel = (idx+1)%len(nums)
            while travel != idx:
                if nums[travel] > nums[idx]:
                    res.append(nums[travel])
                    break
                travel = (travel+1) % len(nums)
            if len(res) < idx+1:
                res.append(-1)
        return res
