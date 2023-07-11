#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        #检查从1到n中有多少5,因为5和2相乘才会出现0,而2的数量远大于5,所以只需要检查5的数量
        #5的倍数有5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90
        ans=0
        for i in range(1,n+1):
            while i%5==0:
                ans+=1
                i//=5
        return ans
# @lc code=end

