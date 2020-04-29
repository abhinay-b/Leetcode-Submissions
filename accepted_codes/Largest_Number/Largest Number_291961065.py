class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
        power = len(str(max(nums)))
        nums = list(map(lambda x:str(x),nums))
        nums.sort(key=(lambda x:x*(power//len(x))+x[:power%len(x)+1]),reverse=True)
        return str(int(''.join(nums)))
        
