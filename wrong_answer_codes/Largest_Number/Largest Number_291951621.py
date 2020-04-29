class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        power = len(str(max(nums)))
        nums = list(map(lambda x:str(x),nums))
        nums.sort(key=(lambda x:x+x[-1]*(power-len(str(x)))),reverse=True)
        return str(int(''.join(nums)))
        
