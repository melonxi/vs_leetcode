#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #使用位运算，异或运算
        #异或运算的性质：两个相同的数异或为0，一个数与0异或为本身
        ans = 0
        for nums in nums:
            ans ^= nums
        return ans
# @lc code=end

