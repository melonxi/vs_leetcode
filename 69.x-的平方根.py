#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        #二分查找,找到最后一个小于等于x的数
        #如果mid*mid <= x,则left = mid + 1
        #否则right = mid
        #最后返回left - 1
        if x == 0:
            return 0    
        left = 1
        right = x
        while left < right:
            mid = (left + right + 1) // 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid - 1
        return left
    
      
# @lc code=end

