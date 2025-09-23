class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = 0
        for i in range(k):
            avg += nums[i]
        res = avg
        for i in range(k, len(nums)):
            avg -= nums[i - k]
            avg += nums[i]
            if res < avg:
                res = avg
        return res / k
