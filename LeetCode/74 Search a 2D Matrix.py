class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m-1
        while l <= r:
            middle = (l+r) // 2
            if matrix[middle][0] > target:
                r = middle - 1
            elif matrix[middle][-1] < target:
                l = middle + 1
            else:
                row = middle
                l, r = 0, n-1
                while l <= r:
                    middle = (l+r) // 2
                    if matrix[row][middle] > target:
                        r = middle - 1
                    elif matrix[row][middle] < target:
                        l = middle + 1
                    else:
                        return True
                return False
        return False
