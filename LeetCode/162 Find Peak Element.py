class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m - 1] < nums[m] and nums[m + 1] < nums[m]:
                return m
            if nums[m - 1] > nums[m] > nums[m + 1]:
                r = m - 1
            else:
                l = m + 1
