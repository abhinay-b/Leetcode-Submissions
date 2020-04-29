class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        def findNum(nums,start,end):
            if start == end:
                if nums[start] == target:
                    return start
                else:
                    return -1
            count = 0
            mid = (start + end) // 2
            last = mid
            while count < 2:
                if target == nums[start]:
                    return start
                elif target == nums[last]:
                    return last
                if target < nums[start]:
                    if target > nums[last] or nums[start] < nums[last]:
                        start = mid+1
                        last = end
                    else:
                        return findNum(nums,start,last)
                else:
                    if target > nums[last]:
                        start = mid+1
                        last = end
                    else:
                        return findNum(nums,start,last)
                count += 1
            return -1
        return findNum(nums,0,len(nums)-1)
