#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        #动态规划，f[n] = f[n-1] + f[n-2]
        #初始化，动态规划数组DP
        DP = [1 for _ in range(n+1)]
        for i in range(n+1):
            if i >= 2:
                DP[i] = DP[i-1]+DP[i-2]
        return DP[n]
# @lc code=end

