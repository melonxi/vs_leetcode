#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        #使用特殊的数字表示状态
        #0: 死细胞转为死细胞
        #1: 活细胞转为活细胞
        #2: 活细胞转为死细胞
        #3: 死细胞转为活细胞
        #遍历矩阵，对每个细胞统计周围活细胞数量，根据规则修改状态，最后再遍历一次矩阵，将2和3转换为1和0
        #时间复杂度O(mn)，
        #空间复杂度O(1)
        m = len(board)
        n = len(board[0])
        #定义方向数组
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                #统计周围活细胞数量
                live = 0
                for direction in directions:
                    r = i + direction[0]
                    c = j + direction[1]
                    if r < 0 or r >= m or c < 0 or c >= n:
                        continue
                    if board[r][c] == 1 or board[r][c] == 2:
                        live += 1
                #规则1和3
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 2
                #规则4
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 3
        #遍历board，将2和3转换为1和0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 1
                        

        """
        Do not return anything, modify board in-place instead.
        """
# @lc code=end

