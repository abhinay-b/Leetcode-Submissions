class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findNum(nums,start,end):
            if (end - start) <= 1:
                if target == nums[start]:
                    return start
                elif target == nums[end]:
                    return end
                else:
                    return -1
            count = 0
            mid = (start + end) // 2
            last = mid
            if target == nums[start]:
                return start
            elif target == nums[mid]:
                return mid
            elif target == nums[end]:
                return end
            while count < 2:
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
                        return findNum(nums,start,mid)
                count += 1
            return -1
        return findNum(nums,0,len(nums)-1)
