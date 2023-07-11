#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        #单调栈解法
        #构建一个数组，模拟单调栈
        stack = []
        #从栈顶到栈底，单调递增
        #当前高度小于栈顶高度时，入栈
        #当前高度大于栈顶高度时，出栈，计算面积
        #当前高度等于栈顶高度是，更新栈，不计算面积
        #栈内只储存位置，不储存高度

        #初始化，首先将第一个位置入栈
        stack.append(0)
        #初始化面积
        area = 0
        #遍历数组
        for i in range(1, len(height)):
            if height[i]<height[stack[-1]]:
                stack.append(i)
            elif height[i]==height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                # 当前高度大于栈顶高度时，出栈，计算面积
                # 直到当前高度小于等于栈顶高度
                while stack and height[i]>height[stack[-1]] :
                    temp = stack.pop()
                    if stack:
                        h = i - stack[-1] - 1
                        w = min(height[i], height[stack[-1]]) - height[temp]
                        area += h*w
                stack.append(i)
        return area


# @lc code=end

