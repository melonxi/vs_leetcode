#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #任何和边缘0相连的0都不会被填充，也就是任何不会和边缘0相连的0都将被填充
        #通过从边缘0进行记忆化搜索，对所有和边缘0相连的0进行特殊标记
        #最后对不是X和特殊标记的0，填充为X
        if not board:
             return None
        def DFS(i,j):
            if i<0 or j<0 or i >=m or j>=n or board[i][j]=="X":
                return
            if board[i][j]=="O":
                board[i][j]="^"
                DFS(i+1,j)
                DFS(i-1,j)
                DFS(i,j+1)
                DFS(i,j-1)

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if i in {0,m-1} or j in {0,n-1}:
                    if board[i][j]=="O":
                        DFS(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                        board[i][j]="X"
        for i in range(m):
            for j in range(n):
                if board[i][j]=="^":
                        board[i][j]="O"

        

        """
        Do not return anything, modify board in-place instead.
        """
# @lc code=end

