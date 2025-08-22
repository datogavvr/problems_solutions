class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        l, r = 10**4, -10**4 # левая и правая границы
        d, u = 10**4, -10**4 # нижняя и верхняя границы
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if j < l:
                        l = j
                    if j > r:
                        r = j
                    if i < d:
                        d = i
                    if i > u:
                        u = i
        return (r-l+1) * (u-d+1)
