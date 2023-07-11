#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        #哈希表，遍历字符串，将每个字符出现的次数存入哈希表，然后再遍历一次字符串，找到第一个出现次数为1的字符
        #时间复杂度O(n)
        #空间复杂度O(n)
        hash = {}
        for c in s:
            hash[c] = hash.get(c, 0) + 1    
        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i
        return -1
# @lc code=end

