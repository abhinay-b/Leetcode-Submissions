class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        left, right = 0, len(nums) - 1
        while(left <= right):
            while(left < right and nums[left] == nums[left+1]):
                left += 1
            while(left < right and nums[right] == nums[right-1]):    
                right -= 1
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == target:
                return True
            if nums[right] == target:
                return True
            if nums[left] < nums[mid]:
                if nums[left] < target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
