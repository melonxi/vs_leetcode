#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0: return -1
        n = len(gas)
        cur_tank = 0
        start = 0
        for i in range(n):
            cur_tank += gas[i] - cost[i]
            if cur_tank < 0:
                start = i + 1
                cur_tank = 0
        return start
# @lc code=end

