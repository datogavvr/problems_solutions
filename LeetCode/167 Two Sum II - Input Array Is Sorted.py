class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}  # target-b -> ind(a)
        for i in range(len(numbers)):
            if numbers[i] in s:
                return [s[numbers[i]] + 1, i + 1]
            else:
                s[target - numbers[i]] = i
