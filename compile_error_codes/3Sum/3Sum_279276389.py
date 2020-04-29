class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            found = False
            res = []
            for i in range(n - 1): 

                # Find all pairs with sum 
                # equals to "-arr[i]" 
                s = set() 
                for j in range(i + 1, n): 
                    x = -(arr[i] + arr[j]) 
                    if x in s: 
                        k = [x, arr[i], arr[j]]
                        k.sort()
                        if k not in res:
                            res.append(k)
                        found = True
                    else: 
                        s.add(arr[j]) 
            return res

