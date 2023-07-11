#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #先遍历一遍矩阵，将矩阵中的0全部标记为None
        #再遍历一遍矩阵，将None所在的行列全部置零
        #别忘了把None再置回0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][j] = float('inf')
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=0
                    for k in range(m):
                        if matrix[k][j]!=float('inf'):
                            matrix[k][j] = 0
                    for k in range(n):
                        if matrix[i][k]!=float('inf'):
                            matrix[i][k] = 0
        

        """
        Do not return anything, modify matrix in-place instead.
        """
# @lc code=end

