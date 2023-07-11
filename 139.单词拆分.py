#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划
        # 1. 状态定义：dp[i]表示s[:i]是否可以拆分
        # 2. 状态转移方程：dp[i] = dp[j] and s[j:i] in wordDict
        # 3. 初始状态：dp[0] = True
        # 4. 返回值：dp[-1]
        # 时间复杂度：O(n^2)，n为字符串长度
        # 空间复杂度：O(n)，n为字符串长度
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
       
        
# @lc code=end

