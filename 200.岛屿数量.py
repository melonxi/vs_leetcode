#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #回溯法
        #从1开始搜索，遇到0结束搜索，搜索过程中遇到的1都置为0
        #注意搜索边界
        if not grid:
            return 0
        ans=0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    ans+=1
                    self.backtrack(grid,i,j)
        return ans
    
    def backtrack(self,grid,i,j):
        # 判断边界和是否为0
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0':
            return
        # 将遇到的1置为0
        grid[i][j]='0'
        # 四个方向进行回溯
        self.backtrack(grid,i+1,j)
        self.backtrack(grid,i-1,j)
        self.backtrack(grid,i,j+1)
        self.backtrack(grid,i,j-1)
        return
    
# @lc code=end

