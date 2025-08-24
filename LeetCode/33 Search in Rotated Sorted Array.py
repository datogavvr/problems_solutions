class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            if nums[l] <= nums[middle]:
                if nums[l] <= target < nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1
            else:
                if nums[middle] < target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1

        return -1