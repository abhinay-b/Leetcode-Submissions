class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        count = 0
        subarr = 0
        start = 0
        for num in nums:
            subarr += num
            while subarr > k:
                subarr -= nums[start]
                start += 1
            if subarr == k:
                count += 1
        return count
