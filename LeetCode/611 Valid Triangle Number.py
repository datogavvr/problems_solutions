class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        res = 0
        for r in range(len(nums)-1, 1, -1):
            l, m = 0, r-1
            while l < m:
                if nums[l]+nums[m] > nums[r]:
                    res += m-l
                    m -= 1
                else:
                    l += 1
        return res
