#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #动态规划
        #循环嵌套，考察左右边界，以及是否相等
        n = len(s)#字符串长度
        if n < 2:
            return s
        max_len = 1
        start = 0

        DP = [[False] * n for _ in range(n)]#初始化DP数组

        for i in range(n):#初始化DP数组
            DP[i][i] = True
        
        for L in range(2,n+1):#L为子串长度
            for i in range(n-L+1):#i为子串起始位置
                j = i+L-1
                if s[i]!=s[j]:
                    DP[i][j] = False
                else:
                    if L<=3:
                        DP[i][j] = True
                    else:
                        DP[i][j] = DP[i+1][j-1]
                if DP[i][j] and L>max_len:
                    max_len = L
                    start = i
        
        return s[start:start+max_len]

        
# @lc code=end

