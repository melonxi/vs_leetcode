#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #小顶堆+归并排序
        #时间复杂度：O(klogn)
        #空间复杂度：O(n)
        import heapq
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)
        for i in range(k-1):
            num, x, y = heapq.heappop(pq)
            if y < n-1:#之所以要判断y是否为n-1，是因为如果y为n-1，那么y+1就会越界
                #每次都是取最小的，所以只需要把当前最小的右边的元素加入堆中
                heapq.heappush(pq, (matrix[x][y+1], x, y+1))    
        return heapq.heappop(pq)[0]
    
# @lc code=end

