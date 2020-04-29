import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return -1        
        n = len(matrix)
        if k > n**2:
            return -1
        size = k
        heap = [] 
        heapq.heapify(heap)
        if n < k:
            size = n
        for j in range(size):
            heapq.heappush(heap,(matrix[0][j],0,j))
        for _ in range(k-1):
            val,i,j = heapq.heappop(heap)
            if i < n-1:
                heapq.heappush(heap,(matrix[i+1][j],i+1,j))
        return heapq.heappop(heap)[0]
