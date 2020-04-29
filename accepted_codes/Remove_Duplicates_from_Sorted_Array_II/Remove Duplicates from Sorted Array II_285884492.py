class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nxt = 0
        same = 1
        for i in range(len(nums)-1):
            if nums[nxt] == nums[i+1]:
                same += 1
                if same > 2:
                    continue           
            else:
                same = 1
            nxt += 1
            nums[nxt],nums[i+1] = nums[i+1],nums[nxt] 
        print(nums)
        return nxt+1
