class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        result = []
        if 0 in d and d[0] > 2:
            result.append([0,0,0])
            
        # pos = set([num for num in nums if num > 0])
        # neg = set([num for num in nums if num < 0])
        
        pos = [num for num in d if num > 0]
        neg = [num for num in d if num < 0]
        
        for p in pos:
            for n in neg:
                other = -(p+n)
                if other in d:
                    if other == p and d[p] > 1:
                        result.append([n,p,p])
                    elif other == n and d[n] > 1:
                        result.append([n,n,p])
                    elif n < other < p:
                        result.append([n,other,p])
        return result
