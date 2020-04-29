import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minLen = self.maxLen = 0
        self.minHeap,self.maxHeap = [],[]
    def addNum(self, num: int) -> None:
        if not self.maxHeap or  -1*self.maxHeap[0] >= num or (self.minHeap and self.minHeap[0] 
            > num):
            heapq.heappush(self.maxHeap,-1*num)
            self.maxLen += 1
        elif not self.minHeap or self.minHeap[0] <= num:
            heapq.heappush(self.minHeap,num)
            self.minLen += 1
        if self.maxLen - self.minLen > 1:
            temp = heapq.heappop(self.maxHeap)
            self.maxLen -= 1
            heapq.heappush(self.minHeap,-1*temp)
            self.minLen += 1
        elif self.minLen - self.maxLen > 1:
            temp = heapq.heappop(self.minHeap)
            self.minLen -= 1
            heapq.heappush(self.maxHeap,temp)
            self.maxLen += 1
        # print(self.minHeap,self.maxHeap,self.minLen,self.maxLen)    
    def findMedian(self) -> float:
        # print(self.minHeap,self.maxHeap,self.minLen,self.maxLen)
        if self.minLen + self.maxLen == 0:
            return -1
        elif self.minLen < self.maxLen:
            return -1*self.maxHeap[0]
        elif self.maxLen < self.minLen:
            return self.minHeap[0]
        else:
            return (-1*self.maxHeap[0] + self.minHeap[0]) / 2
            
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
