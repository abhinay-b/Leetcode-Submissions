import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            diff = heapq.heappop(stones) - heapq.heappop(stones)
            if diff:
                heapq.heappush(stones,diff)
        if stones:
            return stones[0]*-1
        return 0
