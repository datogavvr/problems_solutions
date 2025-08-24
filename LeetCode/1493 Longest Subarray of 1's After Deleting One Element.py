class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        if not 0 in nums:
            return len(nums) - 1
        sliding_window = [0, 0]
        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(res, sum(sliding_window))
                sliding_window = [sliding_window[1], 0]
            else:
                sliding_window[1] += 1
        res = max(res, sum(sliding_window))
        return res


p = Solution()
print(p.longestSubarray([0,1,1,1,0,1,1,0]))