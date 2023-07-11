#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #先斜角交换，再左右交换
        #所谓斜角交换，就是横纵坐标互换
        #所谓左右交换，就是横坐标不变，对称于中轴线的纵坐标互换
        n = len(matrix)
        #斜角交换
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        #左右交换

        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]
                    
            

        


        """
        Do not return anything, modify matrix in-place instead.
        """
# @lc code=end

