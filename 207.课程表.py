#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 使用拓扑排序，判断是否有环
        # 1. 统计每个节点的入度
        # 2. 将入度为0的节点加入队列
        # 3. 遍历队列，将队列中的节点出队，将其指向的节点的入度减1，如果入度为0，加入队列
        # 4. 如果遍历完队列后，所有节点的入度都为0，说明没有环，否则有环
        # 时间复杂度：O(n+m)，n为节点数，m为边数
        # 空间复杂度：O(n+m)，n为节点数，m为边数
        # 入度表
        in_degree = [0] * numCourses
        # 邻接表
        adj = [[] for _ in range(numCourses)]
        # 初始化入度表和邻接表
        for cur, pre in prerequisites:
            in_degree[cur] += 1
            adj[pre].append(cur)
        # 将入度为0的节点加入队列
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        # 遍历队列
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adj[pre]:
                in_degree[cur] -= 1
                if in_degree[cur] == 0:
                    queue.append(cur)
        return numCourses == 0

    
# @lc code=end

