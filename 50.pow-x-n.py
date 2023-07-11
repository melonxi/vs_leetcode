#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #分治递归，从x的n次方转化为x的n/2次方，自底向上，从myPow(1, 0)开始,到myPow(x, n)结束
        #时间复杂度：O(logn)
        #空间复杂度：O(logn)
        #递归出口

        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x, -n)
        #递归
        if n%2==0:
            half =  self.myPow(x, n//2)
            return half*half
        else:
            return x*self.myPow(x, n-1)
        
            
        
# @lc code=end

