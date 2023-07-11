#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #从右上角开始遍历
        #大于目标值就左移，小于目标值就下移
        #如果越界了，就返回False
        #如果相等了，就返回True
        #时间复杂度O(m+n)
        #空间复杂度O(1)
        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while row <= len(matrix) - 1 and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -=1
            else:
                row += 1
        return False
    
        
# @lc code=end

