class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            dictn =  {num:False for num in nums} 
            l = r = maxVal = 1
            for num in nums:
                if not dictn[num]:
                    l,r = num,num
                    while l in dictn:
                        dictn[l] = True
                        l -= 1
                    while r in dictn:
                        dictn[r] = True
                        r += 1
                    maxVal = max(maxVal,(r-l))
            return maxVal-1
                   
