#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import heapq#python中的堆模块,默认是小顶堆,所谓小顶堆就是堆顶元素最小
from heapq import *

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        #python中没有大顶堆,所以需要对数据进行处理，通过存储相反数实现大顶堆
        #所谓大顶堆，就是存入的数会自动将数组中最大的数放在最右边
        #所谓小顶堆，就是存入的数会自动将数组中最小的数放在最左边
        #当大顶堆的长度大于小顶堆的长度时，将大顶堆的堆顶元素放入小顶堆中
        #注意大顶堆的数字是负数，所以要取相反数

        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        #这样操作的原因是要保障small中的数字都小于large中的数字
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0#为什么是-号呢，因为大顶堆的数字是负数，所以要取相反数




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

