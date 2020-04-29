import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        stones = [-1*stones[i] for i in range(len(stones))]
        heapq.heapify(stones)
        while(len(stones)>1):
            diff = heapq.heappop(stones) - heapq.heappop(stones)
            heapq.heappush(stones,diff)
        return -1*stones[0]
