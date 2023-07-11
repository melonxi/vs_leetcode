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
        # 递归,DFS
        # 1. 使用邻接表存储图
        # 2. 从每个节点开始，判断是否有环
        # 3. 如果有环，返回False，否则返回True
        # 时间复杂度：O(n+m)，n为节点数，m为边数
        # 空间复杂度：O(n+m)，n为节点数，m为边数
        # 邻接表
        adj = [[] for _ in range(numCourses)]
        # 初始化邻接表
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        # 用于记录节点的状态，0表示未搜索，1表示搜索中，2表示已完成搜索
        visited = [0] * numCourses
        # 判断是否有环
        def dfs(i):
            # 如果已经搜索过，直接返回True
            if visited[i] == 1:
                return False
            # 如果已经完成搜索，直接返回False
            if visited[i] == 2:
                return True
            # 标记为搜索中
            visited[i] = 1
            # 遍历邻接表
            for j in adj[i]:
                # 如果有环，返回False
                if not dfs(j):
                    return False
            # 标记为已完成搜索
            visited[i] = 2
            return True
        # 从每个节点开始，判断是否有环
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    
# @lc code=end

