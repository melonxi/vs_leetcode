#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #动态规划
        #DP[i][j]代表s的前i个字符能不能和p的前j个字符匹配，即s[:i]和p[:j]能不能匹配
        #讨论p[j-1]的三种情况
        #1. p[j-1] == s[i-1] or p[j-1] == '?'，则DP[i][j] = DP[i-1][j-1]
        #2. p[j-1] == '*'，则DP[i][j] = DP[i-1][j] or DP[i][j-1]，即*匹配0个或多个字符
        #3. 其他情况，DP[i][j] = False
        #初始化
        #DP[0][0] = True，即s和p都为空时，匹配
        #DP[0][j] = DP[0][j-1]，即s为空，p不为空时，只有p[j-1]为*时，才能匹配   
        #DP[i][0] = False，即s不为空，p为空时，不能匹配 
        #时间复杂度O(m*n)，空间复杂度O(m*n)
        m = len(s)
        n = len(p)
        DP = [[False] * (n+1) for _ in range(m+1)]
        DP[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                DP[0][j] = DP[0][j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    DP[i][j] = DP[i-1][j-1]
                elif p[j-1] == '*':
                    DP[i][j] = DP[i-1][j] or DP[i][j-1]
        return DP[m][n]
    
# @lc code=end

