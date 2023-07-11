#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        n = abs(x)
        reverse_n = 0
        while n:
            reverse_n = reverse_n*10 + n%10
            n = n//10
        if x<0:
            reverse_n = -reverse_n
        if reverse_n > 2**31-1 or reverse_n < -2**31:
            return 0
        return reverse_n
# @lc code=end

