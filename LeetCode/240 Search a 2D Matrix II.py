class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(row: list[int], n: int, target: int) -> bool:
            l, r = 0, n-1
            while l <= r:
                middle = (l+r) // 2
                if row[middle] > target:
                    r = middle - 1
                elif row[middle] < target:
                    l = middle + 1
                else:
                    return True
            return False

        for row in matrix:
            if binarySearch(row, len(matrix[0]), target) == True:
                return True
        return False

