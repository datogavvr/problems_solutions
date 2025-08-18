class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        marr =  sorted(nums1 + nums2)
        k = len(nums1) + len(nums2)
        if k % 2 == 0:
            ans = (float(marr[k//2 - 1]) + float(marr[k//2]))/2.0
        else:
            ans = float(marr[k//2])
        return ans