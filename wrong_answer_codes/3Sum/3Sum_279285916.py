class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #return empty list if list size < 3
        if not nums or len(nums) < 3:
            return []

        nums.sort()
        #if the smallest number >0 or largest < 0, we can't have a sum of 0
        if nums[0] > 0 or nums[-1] < 0:
            return []

        res = []

        #find the index of the first non zero element
        non_zero_index = next(index for index,val in enumerate(nums) if val>0)


        #we will keep the pivot index to 0 and iterate till non_zero_index
        for pivot in range(non_zero_index):

            #skip already computed pivots
            if pivot >0 and nums[pivot-1] == nums[pivot]:
                continue

            left = pivot+1
            right = len(nums) -1

            while left < right:
                s = nums[pivot] + nums[left] + nums[right]
                if s > 0:
                    # if sum greater than zero we will move the right pointer towards the left
                        (smaller value)
                    # if the previous element is same , we will skip the that element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -=1
                elif s < 0:
                    # if sum greater less zero we will move the left pointer towards the right
                        (higer value)
                    # if the next element is same , we will skip the that element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left +=1
                else:

                    # if sum is zero, we will append the triplet to list
                    # move both left and right to next position avoiding the duplicates
                    res.append([nums[pivot], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    right -= 1
                    left += 1
        return res
