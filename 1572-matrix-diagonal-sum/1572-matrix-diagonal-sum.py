class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row=len(mat)
        tot=0
        for i in range(row):
            tot += mat[i][i]
            tot += mat[i][row-1-i]
        if row % 2 == 1:
            tot -= mat[row//2][row//2]
        return tot
