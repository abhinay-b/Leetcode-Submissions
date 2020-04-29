class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        res = [-1]*len(nums)
        nxtGrt = [-1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            travel = (i+1)%len(nums)
            while travel != i:
                if nums[travel] > nums[i]:
                    nxtGrt[i] = travel
                    res[i] = nums[travel]
                    break
                elif nxtGrt[travel] == i:
                    break
                elif nxtGrt[travel] != -1:
                    nxtGrt[i] = nxtGrt[travel]
                    res[i] = nums[nxtGrt[travel]]
                    break
                else:
                    travel = (travel+1)%len(nums)
        return res
