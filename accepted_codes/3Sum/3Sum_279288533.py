class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        table = dict()
        for digit in nums:
            if digit not in table:
                table[digit] = 1
            else:
                table[digit] += 1
        res = []
        if 0 in table and table[0] > 2:
            res.append([0,0,0])
        positives = [num for num in table if num > 0]
        negatives = [num for num in table if num < 0]
        for pos in positives:
            for neg in negatives:
                rem = -(pos+neg)
                if rem in table:
                    if rem == pos and table[pos] > 1:
                        res.append([neg,rem,pos])
                    elif rem == neg and table[neg] > 1:
                        res.append([neg,rem,pos])
                    elif neg < rem < pos:
                        res.append([neg,rem,pos])
        return res
