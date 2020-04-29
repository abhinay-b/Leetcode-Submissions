class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        table = dict()
        result = set()
        if len(nums) < 4:
            return []
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
                    for p1 in table[s1]:
                        for p2 in table[s2]:
                            if p1[0] not in p2 and p1[1] not in p2:
                                temp = p1 + p2
                                temp = [nums[i] for i in temp]
                                temp.sort()
                                result.add((temp[0],temp[1],temp[2],temp[3]))
        return [list(i) for i in result]
