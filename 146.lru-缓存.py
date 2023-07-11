#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
from collections import OrderedDict
class LRUCache:
    

    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.cap = capacity
       

    def get(self, key: int) -> int:
        if key in self.dict.keys():
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        #如果key在字典里，就更新value,并把key-value移动到最右边
        if key in self.dict.keys():
            self.dict[key] = value
            self.dict.move_to_end(key)
        else:
            #如果key不在字典里，就看字典长度是否达到上限，如果达到上限，就把最左边的key-value删除，再把新的key-value加入字典
            if len(self.dict) == self.cap:
                self.dict.popitem(last=False)
            self.dict[key] = value
            #self.dict.move_to_end(key)

       
        

        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

