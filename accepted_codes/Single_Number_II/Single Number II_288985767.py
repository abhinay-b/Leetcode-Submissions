class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''General: Every element appears m times except for one, which appears exactly k 
            times. Find that single one.
        Let array length be n. Then elements appear m times each to give (n-1) while 1 element 
            appears n times.
        Let the sum of the m-repeating elements be x (when considered without their duplicates
            ) while the single element value be y.
        Then summing all the elements in the array,
        m*x + n*y = c1
        On summing up only the unique elements,
        x + y = c2
        On solving these 2 pairs of equations, we get:
        y = (mc2 - c1) / (m-n)'''
        m = 3
        n = 1
        return int((m*sum(set(nums)) - sum(nums)) / (m-n))
