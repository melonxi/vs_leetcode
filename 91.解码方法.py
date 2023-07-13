#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] 表示长度为 i 的字符串的解码方法数，对应的字符串为 s[:i]，不包含第 i 个字符
        #当计算dp[i]的值的时候，我们考察s[i-1:i]和s[i-2:i]这两个子串
        #当s[i-1:i]为1-9，它就可以被独立解码，解码的方法数为dp[i-1]
        #当s[i-2:i]为10-26，它就可以被独立解码，解码的方法数为dp[i-2]
        #初始化dp，dp[0] = 1
        #当s[0]不为0时，dp[1] = 1，否则dp[1] = 0
        #最终返回dp[-1]
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            if s[i-1:i] != '0':
                dp[i] += dp[i-1]
            if '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]
        return dp[-1]
    



# @lc code=end

