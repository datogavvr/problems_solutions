import numpy as np

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:  
        m = len(matrix) # количество строк
        n = len(matrix[0]) # количество столбцов
        sm = [[0] * (n+1) for i in range(m+1)] # матрица максимальных квадратов
        total = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    sm[i + 1][j + 1] = min(sm[i][j+1], sm[i+1][j], sm[i][j]) + 1
                    total += sm[i+1][j+1]
        return total