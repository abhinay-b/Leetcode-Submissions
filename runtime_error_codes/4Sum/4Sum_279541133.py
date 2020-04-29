class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pairs = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                pairs[nums[i] + nums[j]].append((i,j))
                
        solution = set()
        for key in pairs:
            if (target-key) in pairs:
                for x, y in pairs[key]:
                    for j, k in pairs[target-key]:
                        if x != j and y != k and x != k and y != j:
                            answer = sorted([nums[x],nums[y],nums[j], nums[k]])
                            solution.add((answer[0],answer[1],answer[2],answer[3]))
                            
        return [list(i) for i in solution]
