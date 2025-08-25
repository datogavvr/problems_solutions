class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        arr = []
        m = len(mat)
        n = len(mat[0])
        mark = True
        s = 0 # сумма индексов в диагонали
        while s != m+n-1:
            if mark: # диагональ вправо вверх
                if s < m:
                    current = [s, 0]
                else:
                    current = [m-1, s-m+1]
                while not (current[0] < 0 or current[1] > n-1):
                    arr.append(mat[current[0]][current[1]])
                    current[0] -= 1
                    current[1] += 1
                mark = False
            else: # диагональ влево вниз
                if s < n:
                    current = [0, s]
                else:
                    current = [s-n+1, n-1]
                while not (current[0] > m-1  or current[1] < 0):
                    arr.append(mat[current[0]][current[1]])
                    current[0] += 1
                    current[1] -= 1
                mark = True
            s += 1
        return arr