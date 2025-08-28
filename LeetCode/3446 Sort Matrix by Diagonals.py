class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        grid = [i for i in grid]
        for i in range(n):
            ind = [i, 0]
            lt = [] # диагональ левого треугольника
            rt = [] # диагональ правого треугольника

            while ind[0] < n: # заполняем диагонали
                lt.append(grid[ind[0]][ind[1]])
                if i > 0:
                    rt.append(grid[ind[1]][ind[0]])
                ind[0] += 1
                ind[1] += 1
            lt.sort(reverse=1)
            rt.sort()

            ind = [i, 0]
            while ind[0] < n: # добавляем диагонали в матрицу
                grid[ind[0]][ind[1]] = lt[ind[1]]
                if i > 0:
                    grid[ind[1]][ind[0]] = rt[ind[1]]
                ind[0] += 1
                ind[1] += 1
        return grid



