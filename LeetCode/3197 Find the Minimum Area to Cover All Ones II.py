import numpy as np

class Solution:
    def minimumSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        l, r = 10**4, -10**4 # левая и правая границы
        u, d = 10**4, -10**4 # верхняя и нижняя границы
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if j < l:
                        l = j
                    if j > r:
                        r = j
                    if i > d:
                        d = i
                    if i < u:
                        u = i
        print(u, d, l, r)
        print(grid)
        grid = np.array(grid)[u:d+1, l:r+1]
        print(grid)
        return (r-l + 1) * (u-d + 1)

p = Solution.minimumSum(1, [[1,0,1,0],[0,1,0,1],[0,0,0,0]])
print(p)