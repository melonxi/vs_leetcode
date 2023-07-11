#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start

class MinStack:
    #双栈法

   

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []#数据栈
        self.min_stack = []#
       
    def push(self, val: int) -> None:
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)

       
    def pop(self) -> None:  
        if self.stack:
            if self.stack.pop() == self.min_stack[-1]:
                self.min_stack.pop()


  


    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None

        




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

