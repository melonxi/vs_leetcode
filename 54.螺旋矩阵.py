#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        ans = []
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        while True:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            for j in range(top,bottom+1):
                ans.append(matrix[j][right])
            right-=1
            if right < left:
                break
            for k in range(right,left-1,-1):
                ans.append(matrix[bottom][k])
            bottom-=1
            if bottom < top:
                break
            for l in range(bottom,top-1,-1):
                ans.append(matrix[l][left])
            left+=1
            if left>right:
                break 

        return ans
        
# @lc code=end

