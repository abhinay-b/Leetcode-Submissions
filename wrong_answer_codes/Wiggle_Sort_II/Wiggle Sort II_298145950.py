class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        res = nums.copy()
        nums.clear()
        left,right = 0,(len(res)+1)//2
        curr = right
        while left < curr:
            # print(res)
            nums.append(res[left])
            if right < len(res):
                nums.append(res[right])
                right += 1
            left += 1
