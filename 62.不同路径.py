#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #动态规划
        #DP[i][j]代表到达[i,j]坐标的可能路径总数
        #DP[i][j] = DP[i-1][j]+DP[i][j-1]
        #第一行和第一列都是1
        #时间复杂度：O(m*n)
        #空间复杂度：O(m*n)
        if m==0 or n==0:
            return 0
        DP = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                DP[i][j] = DP[i-1][j]+DP[i][j-1]
        return DP[-1][-1]
    
# @lc code=end

