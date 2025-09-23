class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        if len(mat) == 1:
            return mat[0][0]
        for i in range(len(mat)):
            res += mat[i][i] + mat[len(mat)-i-1][i]
        if len(mat) % 2 == 1:
            res -= mat[len(mat)//2][len(mat)//2]
        return res
