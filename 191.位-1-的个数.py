#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        #利用位运算的性质
        #一个数n如果减去1，那么会使得从右往左第一个1之前的所有位取反
        #再进行n和n-1的与运算，就会让从右往左第一个1，包括它自己，都变成0，也就等于每次都会从右往左消去一个1
        #每次消去一个1，计数器加1，直到n变成0
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
        
# @lc code=end

