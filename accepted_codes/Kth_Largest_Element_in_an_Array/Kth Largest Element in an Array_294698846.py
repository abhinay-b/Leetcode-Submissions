import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) < k or k == 0:
            return -1
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k,len(nums)):
            if heap[0] < nums[i]:
                heapq.heappushpop(heap,nums[i])
        return heap[0]
        
