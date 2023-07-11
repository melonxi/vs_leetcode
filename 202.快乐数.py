#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        #哈希表，记录每次计算的结果，如果出现重复的结果，则说明陷入了循环，不是快乐数
        #时间复杂度O(logn)，空间复杂度O(logn)
        if n == 1:
            return True
        hashset = set()
        while n != 1:
            if n in hashset:
                return False
            hashset.add(n)
            n = self.get_next(n)
        return True
    def get_next(self, n):
        next = 0
        while n > 0:
            n, digit = divmod(n, 10)#divmod()函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
            next += digit ** 2
        return next
# @lc code=end

