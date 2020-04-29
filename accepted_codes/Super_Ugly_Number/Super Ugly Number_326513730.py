import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        arr = [1]
        uglies = set()
        heapq.heapify(arr)
        count = 0
        while count < n:
            num = heapq.heappop(arr)
            count += 1
            for prime in primes:
                newNum = num*prime
                if newNum not in uglies:
                    uglies.add(newNum)
                    heapq.heappush(arr,newNum)
        return num
