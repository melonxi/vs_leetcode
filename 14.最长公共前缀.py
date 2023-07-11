#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #暴力扫描
        if len(strs) == 0:
            return ""
        
        word_nums = len(strs)
        for i in range(len(strs[0])):
            for j in range(1,word_nums):
                if i > len(strs[j])-1 or strs[j][i]!=strs[0][i]:
                    return strs[0][:i] 
        return strs[0]                
# @lc code=end

