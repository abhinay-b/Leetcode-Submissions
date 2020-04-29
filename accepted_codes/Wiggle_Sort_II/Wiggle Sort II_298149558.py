class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        res = nums.copy()
        nums.clear()
        left,right = (len(res)-1)//2,len(res)-1
        curr = left
        while left >= 0:
            # print(res)
            nums.append(res[left])
            if right > curr:
                nums.append(res[right])
                right -= 1
            left -= 1
