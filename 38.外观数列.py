#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        def explain(s):
            i = 0
            res = ''
            while i < len(s):
                count = 1#这里代表有几个相同的数字,初始值为1，因为至少有一个
                while i< len(s)-1 and s[i]==s[i+1]:
                    count += 1#由于循环条件，所以只要进入循环，就代表有两个相同的数字，就要加1
                    i += 1
                res += str(count) + s[i]
            return res
        res = '1'
        for i in range(n-1):#这里代表解释次数，初始已经解释了一次，从0->n-2,解释了n-1次，再加上一开始的初始值，就是n次
            res = explain(res)
        return res
    
# @lc code=end

