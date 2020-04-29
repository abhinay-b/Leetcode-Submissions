from bisect import insort
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.length = 0
        self.nums = []

    def addNum(self, num: int) -> None:
        insort(self.nums,num)
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2:
            return self.nums[self.length//2]
        return (self.nums[self.length//2] + self.nums[self.length//2-1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
