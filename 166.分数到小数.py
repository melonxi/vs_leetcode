#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        #解题关键是找到循环节
        #首先确定符号
        #然后确定有没有小数，通过比较int(numerator/denominator)和numerator/denominator的大小关系
        #然后对于小数部分，通过余数来确定循环节
        if numerator == 0:
            return '0'
        sign = (numerator>0) is (denominator>0)#True是正数，False是负数
        numerator, denominator = abs(numerator), abs(denominator)
        integer = numerator//denominator
        remainder = numerator%denominator
        #开始判断是否有小数，小数中的循环节从余数重复出现开始，到下一个余数重复出现结束，这里的余数是余数乘以10除以除数得到的，第一个余数是numerator%denominator，其位置是0
        #小数部分的开始，是整数部分计算完毕后，余数不为0，开始计算小数部分，所以需要判断余数是否为0
        #每一位小数计算，都是余数乘以10除以除数得到的，第一个余数是numerator%denominator，其位置是0，注意这里的位置，其实指的是小数部分每一个数字的位置，不是余数的位置
        if remainder == 0:
            return str(integer) if sign else '-'+str(integer)
        else:#有小数，需要找循环节，用字典来记录余数和对应的位置，如果出现重复的余数，说明有循环节
            decimal = []#小数部分，用列表来存储，最后用join来连接
            remainder_dict = {}#用字典来存储余数和对应的位置，如果出现重复的余数，说明有循环节
            while remainder != 0:#余数为0说明除尽了，没有循环节
                if remainder in remainder_dict:#出现重复的余数，说明有循环节
                    decimal.insert(remainder_dict[remainder], '(')#在循环节开始的位置插入'('
                    decimal.append(')')#在循环节结束的位置插入')'
                    break#跳出循环
                remainder_dict[remainder] = len(decimal)#记录余数和对应的位置
                remainder *= 10#余数乘以10，然后除以除数，得到商和余数
                decimal.append(str(remainder//denominator))#商加入到小数部分
                remainder %= denominator#更新余数
            return str(integer)+'.'+''.join(decimal) if sign else '-'+str(integer)+'.'+''.join(decimal)#最后用join来连接

# @lc code=end

