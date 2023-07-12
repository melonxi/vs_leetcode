#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #倍增法
        sign  = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp,i = divisor,1
            while temp<= dividend:
                dividend-=temp
                res+=i
                temp<<=1
                i<<=1
    
        if not sign:
            res = -res
        return min(max(-2**31, res), 2**31-1)
    
    
        
    
    

# @lc code=end

