class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diff) < 0:
            return -1
        start = 0
        total = 0
        for i in range(len(gas)):
            total += diff[i]
            if total <= 0:
                start = i
                total = diff[i]
        if diff[start] < 0:
            return (start+1)%len(gas)
        return start
                    
