class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[left] < target:
                if nums[left] < target and nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left = mid + 1
        return -1
