#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #双端队列，队列中存储的是元素的下标，队列中的元素是单调递减的
        #当队列中的元素个数大于k时，队首元素出队
        #当队列中的元素个数小于k时，队尾元素入队
        #队首元素即为当前窗口的最大值
        from collections import deque#双端队列
        if len(nums) < 2:#特殊情况
            return nums
        res = []#存储结果
        queue = deque()#双端队列,存储元素的下标,队列中的元素是单调递减的,队首元素即为当前窗口的最大值
        for i in range(len(nums)):#遍历数组,维护双端队列,存储当前窗口的最大值
            #当i小于k-1时，双端队列处于初始化阶段，滑动窗口未形成，此时只需要维护双端队列即可,不需要将队首元素加入到res中,因为此时的队首元素并不是当前窗口的最大值
            #一旦i大于等于k-1时，双端队列处于维护阶段，此时需要将队首元素加入到res中,因为此时的队首元素即为当前窗口的最大值
            if queue and queue[0] == i-k:#当i-k等于queue[0]时，说明双端队列的队首处的值，已经不在当前的滑动窗口中，因此该值无效，需要出队
                queue.popleft()#队首元素出队
            while queue and nums[queue[-1]] < nums[i]:#队列中的元素是单调递减的,当队尾元素小于nums[i]时,队尾元素出队
                queue.pop()#队尾元素出队
            queue.append(i)#队尾元素入队
            if i >= k-1:#当i>=k-1时,队首元素即为当前窗口的最大值
                res.append(nums[queue[0]])#队首元素即为当前窗口的最大值
        return res
        







# @lc code=end

