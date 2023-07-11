#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划,DP[i]代表字符串的前i个字符是否可以拆分成字典中的单词
        # 如果DP[j]为True，且s[j+1:i]在字典中，那么DP[i]为True
        # DP初始化为False,长度为n+1
        # DP[0]为True,空字符串可以被拆分
        # 时间复杂度O(n^2),空间复杂度O(n)
        n = len(s)
        DP = [False] * (n + 1)
        DP[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if DP[j] and s[j:i] in wordDict:
                    DP[i] = True
                    break
        return DP[-1]
# @lc code=end

