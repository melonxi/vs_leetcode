#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #记忆化搜索，DFS
        #创建一个visited矩阵，用于存储元素状态，如果是访问过的元素，就不再访问，既可以防止重复访问，也可以防止重复使用
        #当搜索周围元素时，如果周围元素不符合要求，就回溯，如果都不符合要求，就终止当前搜索，相当于剪枝
        #DFS使用一个位置参数，用于记录搜索到word的第几个元素，如果搜索到最后一个元素，就返回True

        word_len = len(word)
        row = len(board)
        col = len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        def dfs(i,j,k):#i,j为当前位置，k为当前搜索到word的第几个元素
            if k==word_len:
                return True
            if i<0 or i>=col or j<0 or j>=row or visited[j][i] or board[j][i]!=word[k]:
                return False
            visited[j][i] = True
            res = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            visited[j][i] = False#回溯
            return res
        for i in range(col):
            for j in range(row):
                if dfs(i,j,0):
                    return True
        return False
    
# @lc code=end

