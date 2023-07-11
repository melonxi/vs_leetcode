#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [0] + [amount + 1] * amount
        for i in range(amount + 1):
            for coin in coins:
                if i>=coin:
                    DP[i] = min(DP[i-coin]+1,DP[i])
        
        return DP[amount] if DP[amount] < amount+1 else -1


# @lc code=end

