#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 一次遍历
        # 用set记录，如果有重复的数字，就返回False
        helper_row = [set() for _ in range(9)]
        helper_col = [set() for _ in range(9)]
        helper_block = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    block_index = (i // 3) * 3 + j // 3# 用这个公式计算块的索引,是一种映射关系
                    if num in helper_row[i] or num in helper_col[j] or num in helper_block[block_index]:
                        return False
                    helper_row[i].add(num)
                    helper_col[j].add(num)
                    helper_block[block_index].add(num)

# @lc code=end

