from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictnNum = defaultdict(int)
        dictnVal = defaultdict(list)
        arr = []
        res = []
        for num in nums:
            dictnNum[num] += 1
        for key,val in dictnNum.items():
            dictnVal[val].append(key)
        arr = list(dictnNum.values())
        heap = []
        for i in range(k):
            heapq.heappush(heap,-arr[i])
        for i in range(k+1,len(arr)):
            num = heapq.heappushpop(heap,-arr[i])
        for val in set(heap):
            if len(res) < k:
                res += dictnVal[-val][:k-len(res)]
            else:
                break
        return res
