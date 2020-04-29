import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        factors = [2,3,5]
        arr = [1]
        nums = set()
        heapq.heapify(arr)
        res = count = 0
        idx = 0
        while count < n:
            num = heapq.heappop(arr)
            # print(num)
            count += 1
            for i in range(3):
                newNum = num*factors[i]
                if newNum not in nums:
                    nums.add(newNum)
                    heapq.heappush(arr,newNum)
        return num
