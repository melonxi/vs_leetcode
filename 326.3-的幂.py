#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #不使用循环或者递归
        #时间复杂度O(1)
        #空间复杂度O(1)
        #1162261467是3的19次幂，是int范围内最大的3的幂
        #如果n是3的幂，那么1162261467一定能被n整除

        return n > 0 and 3**19 % n == 0
    
    
# @lc code=end

