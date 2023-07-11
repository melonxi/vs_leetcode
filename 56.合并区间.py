#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #如果当前区间的end大于下一个区间的start,则合并
        #否则不合并
        #排序，按照区间的start排序
        intervals.sort(key=lambda x:x[0])
        res = []
        for i in range(len(intervals)):
            #如果intervals为空，或者res的最后一个区间的end小于当前区间的start
            #则直接将当前区间加入res
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                #否则，则说明当前区间和res的最后一个区间有重叠
                #将当前区间合并到res的最后一个区间
                #由于res的最后一个区间的end可能小于当前区间的end
                #所以需要取最大值
                res[-1][1] = max(res[-1][1],intervals[i][1])
        return res
    
# @lc code=end

