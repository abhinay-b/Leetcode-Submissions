import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minLen = self.maxLen = 0
        self.minHeap,self.maxHeap = [],[]
    def addNum(self, num: int) -> None:
        if self.maxLen == self.minLen:
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap,num))
            self.maxLen += 1
        else:
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap,-num))
            self.minLen += 1
        # print(self.minHeap,self.maxHeap,self.minLen,self.maxLen)    
    def findMedian(self) -> float:
        # print(self.minHeap,self.maxHeap,self.minLen,self.maxLen)
        if self.minLen + self.maxLen == 0:
            return -1
        elif self.minLen == self.maxLen:
            return (-1*self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return -1*self.maxHeap[0]
        
            
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
