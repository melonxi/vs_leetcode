#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
        def largestRectangleArea(self, heights: List[int]) -> int:
            #维护一个递增的栈，用于寻找以栈顶元素高为矩形高的最大的面积的左右边界
            #通俗的说，如果想以当前的高围成矩形，那么左右高就应该高于当前的高度
            #当我们维护一个递增栈时，我们可以确定，栈顶左边元素所指向的高一定低于栈顶高，形成了左边界
            #当我们遍历数组时，一旦发现比栈顶矮的元素，就可以确定，该位置是当前栈顶的最大面积的右边界
            #因此，我们需要得到左右边界之间的宽度，用于计算面积
            #另外我们需要一个特殊值，用于模拟左边界，该左边界为负值，方便我们循环代码的编写
            #其次，当我们遍历完数组之后，如果栈内还有元素，还需要以栈内元素为高进行计算，左边界为-1，右边界为数组长度+1

             # 初始化最大面积
            max_area = 0
            # 创建一个单调栈
            stack = [-1]
            # 遍历每一个柱子
            for i in range(len(heights)):
                # 当栈非空并且当前柱子的高度小于栈顶柱子的高度
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    # 弹出栈顶柱子并更新最大面积
                    max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))#注意stack.pop()，stack[-1]已经是之前栈顶左边元素了
                # 将当前柱子入栈
                stack.append(i)
            # 处理栈中剩余的柱子
            while stack[-1] != -1:
                # 弹出栈顶柱子并更新最大面积
                max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
            # 返回最大面积
            return max_area

                

# @lc code=end

