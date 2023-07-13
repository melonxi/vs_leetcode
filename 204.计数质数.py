#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        #什么是质数：只能被1和自身整除的数
        #质数的倍数一定不是质数
        #时间复杂度O(nlogn)
        #空间复杂度O(n)
        if n < 2:
            return 0
        #初始化一个长度为n的数组，用于标记是否为质数
        isPrime = [1] * n
        #0和1不是质数
        isPrime[0] = isPrime[1] = 0
        #遍历数组，如果是质数，那么它的倍数一定不是质数
        for i in range(2, int(n ** 0.5) + 1):#这里的+1是因为range的右边界是开区间，不包括n
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * len(isPrime[i * i:n:i])
        return sum(isPrime)
    
# @lc code=end

