class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        candidate = -1
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
