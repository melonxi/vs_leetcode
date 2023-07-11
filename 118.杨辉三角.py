#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #每层长度和层数相同
        #每层起始都为1
        #当前层从i为1算起，cur[i] = pre[i-1]+pre[i]
        ans = []
        if not numRows:
            return ans
        if numRows>0:
            ans.append([1])
        if numRows>1:
            for layer_n in range(2,numRows+1):
                cur_layer = [0]*layer_n
                cur_layer[0] = 1
                cur_layer[-1] = 1
                #print(cur_layer,ans)
                if layer_n>2:
                    for i in range(1,layer_n-1):
                        cur_layer[i] = ans[-1][i-1]+ans[-1][i]
                ans.append(cur_layer)
                
        
        return ans
# @lc code=end

