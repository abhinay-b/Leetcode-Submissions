class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nxt = 0
        same = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                same += 1
                if same < 3:
                    nxt += 1
            else:
                nums[nxt+1],nums[i+1] = nums[i+1],nums[nxt+1]
                nxt += 1
                same = 1
        print(nums)
        return nxt+1
