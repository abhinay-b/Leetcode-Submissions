from functools import reduce 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return reduce(lambda x,y : x^y,nums)
