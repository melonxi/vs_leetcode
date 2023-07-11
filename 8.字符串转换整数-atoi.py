#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        #四个步骤
        #1.去除前导空格，可以使用python的字符串strip()函数,该函数可以去除字符串前后的空格
        #2.判断正负，当去除掉前导空格后，会出现三种情况，第一是负号，第二是正号，第三是无符号，前面两个是取s[1:]
        #3.遍历字符串，读字符，累计计算，使用int()函数将字符转换为数字,不是数字就break
        #4.判断溢出，如果在2**32-1之内，返回数字，否则返回2**32-1或者-2**32
        s = s.strip()
        if not s:
            return 0
        ans = 0
        sign = True
        if s[0] == "-":
            sign = False
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        for c in s:
            if c.isdigit():
                ans = ans*10 + int(c)
            else:
                break

        ans = ans if sign else -ans
        
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 - 1:
            return 2**31 - 1
        else:
            return ans

# @lc code=end

