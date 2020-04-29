import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        arr = [1]
        heapq.heapify(arr)
        count = 0
        while count < n:
            num = heapq.heappop(arr)
            count += 1
            for prime in primes:
                heapq.heappush(arr,num*prime)
#               if the current number is a multiple of prime, don't multiply with other primes 
    to avoid duplicates
                if num % prime == 0:
                    break
        return num
