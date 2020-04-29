class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        table = dict()
        for digit in nums:
            if digit not in table:
                table[digit] = 1
            else:
                table[digit] += 1
        result = []
        for idx,digit in enumerate(nums):
            for nxtdigit in nums[idx+1:]:
                k = []
                remain = 0 - (digit + nxtdigit)
                if remain in table:
                    if remain == digit and remain == nxtdigit:
                        if table[remain] > 2:
                            k = [remain,digit,nxtdigit]
                    elif remain == digit or remain == nxtdigit:
                        if table[remain] > 1:
                            k = [remain,digit,nxtdigit]
                    else:
                        k = [remain,digit,nxtdigit]
                    k.sort()
                    if len(k) > 0 and k not in result:
                        result.append(k)
        return result
