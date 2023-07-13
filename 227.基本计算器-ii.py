#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        #栈，遍历s，从左到右依次入栈，当栈顶时*，/时，弹出符号，然后计算栈顶和当前值的结果，再入栈
        #当栈顶时+，-时，弹出符号，然后计算栈顶和当前值的结果，再入栈
        #最后将栈中的值相加即可
        #注意存在连续的数字字符的情况，需要将其转换为数字
        stack = []
        nums = 0
        sign = "+"
        n = len(s)
        for i in range(n):
            if s[i].isdigit():
                nums = nums*10+ int(s[i])
            if s[i] in {"+","-","*","/"} or i == n-1:
                if sign == "+":
                    stack.append(nums)
                elif sign == "-":
                    stack.append(-nums)
                elif sign == "*":
                    stack.append(nums*stack.pop())
                elif sign == "/":
                    stack.append(int(stack.pop()/nums))
                sign = s[i]
                nums = 0
        return sum(stack)
                
    

# @lc code=end

