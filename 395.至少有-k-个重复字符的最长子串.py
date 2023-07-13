#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有 K 个重复字符的最长子串
#

# @lc code=start
import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        #分治法
        if len(s)<k:
            return 0
        counter = collections.Counter(s)

        if min(counter.values())>=k:
            return len(s)

        for c in counter:
            if counter[c]<k:
                return max(self.longestSubstring(sub,k) for sub in s.split(c))
            

# @lc code=end

