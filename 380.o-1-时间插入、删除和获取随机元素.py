#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
import random
class RandomizedSet:
    #使用哈希表+动态数组
    #哈希表存储数字和其在数组中的位置
    #数组存储数字
    #insert操作：先判断数字是否在哈希表中，如果在，返回False，如果不在，将数字插入数组末尾，更新哈希表
    #remove操作：先判断数字是否在哈希表中，如果不在，返回False，如果在，将数字和数组末尾数字交换，更新哈希表，删除数组末尾数字
    #getRandom操作：随机返回数组中的一个数字

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.val2idx = dict()


    def insert(self, val: int) -> bool:
        if val not in self.val2idx:
            self.nums.append(val)
            self.val2idx[val] = len(self.nums)-1
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.val2idx:
            idx = self.val2idx[val]
            self.val2idx[self.nums[-1]] = idx
            self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
            self.nums.pop()
            self.val2idx.pop(val)
            return True
        return False


    def getRandom(self) -> int:
        return random.choice(self.nums)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

