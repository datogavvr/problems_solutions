class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l+r) // 2
            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            elif middle == l:
                res[0] = l
                break
            elif nums[middle-1] != target:
                res[0] = middle
                break
            else:
                r = middle - 1

        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l+r) // 2
            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            elif middle == r:
                res[1] = r
                break
            elif nums[middle+1] != target:
                res[1] = middle
                break
            else:
                l = middle + 1
        return res