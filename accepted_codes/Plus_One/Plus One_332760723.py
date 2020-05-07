class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        carry = 1
        nums = nums[::-1]
        for idx,num in enumerate(nums):
            temp = num + carry
            nums[idx] = temp % 10
            carry = temp // 10
            if carry == 0:
                break
        if carry > 0:
            nums.append(carry)
        return nums[::-1]
