class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = 0 # длина текущей подстроки
        res = 0
        if nums[0] == 0:
            l += 1
            res += l
        for i in range(1, len(nums)):
            if nums[i] == 0 and nums [i-1] == 0:
                l += 1
                res += l
            elif nums[i] == 0:
                l = 1
                res += l
        return res
