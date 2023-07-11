#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #动态规划
        #DP[i][j]表示s的前i个字符和p的前j个字符是否匹配
        #状态转移方程：
        #s[i-1]和p[j-1]代表DP[i][j]的最后一个字符
        #1.当s[i-1]==p[j-1]的时候，DP[i][j] = DP[i-1][j-1]
        #2.当p[j-1]=="."的时候，DP[i][j] = DP[i-1][j-1]
        #3.当p[j-1]=="*"的时候，存在三种情况：
        #   3.1 当p[j-2]!=s[i-1]或者p[j-2]!="."的时候，DP[i][j]= DP[i][j-2]
        #   3.2 当p[j-2]==s[i-1]或者p[j-2]=="."的时候，DP[i][j]= DP[i-1][j] or DP[i][j-2]

        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        #初始化,dp[0][0]表示s和p都为空的时候，为True
        dp[0][0] = True
        for j in range(2,n+1):
            if p[j-1] == '*':#当p的第j个字符为*的时候，dp[0][j]的值和dp[0][j-2]的值相同
                dp[0][j] = dp[0][j-2]
        #状态转移
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        #dp[i][j] = dp[i][j - 2] or dp[i - 1][j]  #降维写法
                        dp[i][j]=dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[-1][-1]
# @lc code=end

