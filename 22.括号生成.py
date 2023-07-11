#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # 通过括号组合规律在DFS过程中进行合法性判断，从而实现剪枝，无需单独的合法性判断程序
        # Use the combination rules of parentheses to perform validity judgment during the DFS process, 
        # thereby achieving pruning and eliminating the need for a separate validity judgment program
        
        res = []

        def DFS(s,left_n,right_n):
            # 如果左括号数量或右括号数量超过n，或者右括号数量大于左括号数量，则返回
            # If the number of left or right parentheses exceeds n, or the number of right parentheses is greater than the number of left parentheses, return
            if left_n>n or right_n>n or right_n > left_n:
                return
            # 如果左括号数量和右括号数量都等于n，则将当前字符串加入结果列表
            # If the number of left and right parentheses are both equal to n, add the current string to the result list
            if left_n==n and right_n ==n:
                res.append(s)
            
            # 递归调用DFS函数，分别添加左括号和右括号
            # Recursively call the DFS function, adding left and right parentheses respectively
            DFS(s+"(",left_n+1,right_n)
            DFS(s+")",left_n,right_n+1)
        
        # 调用DFS函数，初始字符串为空，左右括号数量均为0
        # Call the DFS function, the initial string is empty, and the number of left and right parentheses is both 0
        DFS("",0,0)

        return res



    
        
# @lc code=end

