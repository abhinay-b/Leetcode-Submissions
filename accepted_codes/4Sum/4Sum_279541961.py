from collections import defaultdict

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        table = dict()
        result = set()
        if len(nums) < 4:
            return result
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                pair = nums[i] + nums[j]
                if pair in table:
                    table[pair].append([i,j])
                else:
                    table[pair] = [[i,j]]
            for s1 in table:
                s2 = target - s1
                if s2 in table:
                    for x1,y1 in table[s1]:
                        for x2,y2 in table[s2]:
                            if x1 != x2 and y1 != y2 and x1 != y2 and x2 != y1:
                                temp = [nums[x1], nums[x2], nums[y1], nums[y2]]
                                temp.sort()
                                result.add((temp[0],temp[1],temp[2],temp[3]))
        return result
