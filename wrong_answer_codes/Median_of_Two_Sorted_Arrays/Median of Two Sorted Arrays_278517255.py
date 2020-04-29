class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        start = 1
        end = len(nums1)
        total = len(nums1) + len(nums2) 
        mid = (total) // 2
        while True:
            indexA = (start + end) // 2
            indexB = mid - indexA
            if indexA == 0:
                ALeft = -float("inf")
                ARight = nums1[0]
                BLeft = nums2[mid-1]
                BRight = nums2[mid]
            elif indexA == len(nums1):
                ARight = float("inf")
                ALeft = nums1[-1]
                BLeft = nums2[mid - len(nums1) -1]
                BRight = nums2[mid - len(nums1)]
            else:
                ALeft = nums1[indexA - 1]
                ARight = nums1[indexA]
                BLeft = nums2[indexB - 1]
                BRight = nums2[indexB]
            #print(ALeft, ARight, BLeft, BRight)
            if ALeft > BRight:
                end = indexA-1
            elif BLeft > ARight:
                start = indexA + 1
                end = len(nums1)
            else:
                break
        if total % 2 > 0:
            return min(ARight, BRight)
        else:
            return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
