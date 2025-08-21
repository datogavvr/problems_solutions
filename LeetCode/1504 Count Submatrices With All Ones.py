import numpy as np

class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        m = len(mat)  # количество строк
        n = len(mat[0])  # количество столбцов
        sm1 = [[0] * n for i in range(m)]  # матрица саппортик
        total = 0
        for i in range(m):
            for j in range(n):
                if j == 0:
                    sm1[i][j] = mat[i][j]
                else:
                    if mat[i][j] == 1:
                        sm1[i][j] = (sm1[i][j-1] + 1)
                    else:
                        sm1[i][j] = 0
                sub = sm1[i][j] # количество субматриц с этой клеткой в углу
                for k in range(i, -1, -1):
                    sub = min(sub, sm1[k][j])
                    if sub == 0:
                        break
                    total += sub
        return total


print(Solution.numSubmat(1, [[1,1,1,1,0],[1,0,0,1,0],[0,0,1,0,1],[0,1,0,0,0]]))