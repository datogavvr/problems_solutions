class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            middle = (l+r) // 2
            if arr[middle-1] <= arr[middle] >= arr[middle+1]:
                return middle
            elif arr[middle-1] > arr[middle]:
                r = middle
            elif arr[middle+1] > arr[middle]:
                l = middle
        return middle