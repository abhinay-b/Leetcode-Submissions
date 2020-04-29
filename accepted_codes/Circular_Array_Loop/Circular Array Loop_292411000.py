class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        start = 0
        sign = 1
        n = len(nums)
        visited = set()
        while start < n:
            if start in visited:
                start += 1
                continue
            if nums[start] < 0:
                pos = -1
            else:
                pos = 1
            slow = fast = start
            while True:                
                slow = (slow+nums[slow]) % n
                fast = (fast+nums[fast]) % n
                if nums[fast]*pos <= 0:
                    break
                fast = (fast+nums[fast]) % n
                if nums[slow]*pos <= 0 or nums[fast]*pos <= 0:
                    break
                visited.add(fast)
                visited.add(slow)
                if nums[slow] % n == 0 or nums[fast] % n == 0:
                    break
                if slow == fast:
                    return True
            start += 1
        return False
