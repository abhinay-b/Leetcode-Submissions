import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        factors = [2,3,5]
        arr = [1]
        heapq.heapify(arr)
        res = count = 0
        idx = 0
        while count < n:
            num = heapq.heappop(arr)
            # print(num)
            count += 1
            for prime in factors:
                heapq.heappush(arr,num*prime)
#               if the num is a multiple of current prime, multiplying with other primes will 
    create duplicates
                if num % prime == 0:
                    break
        return num
