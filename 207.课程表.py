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
        #DFS,回溯法
        # 1. 使用邻接表存储图
        # 2. 遍历每个节点，如果节点没有被访问过，就从该节点开始深度优先遍历
        # 3. 在深度优先遍历的过程中，如果遇到已经访问过的节点，说明有环，返回False
        # 4. 如果遍历完所有节点都没有遇到已经访问过的节点，说明没有环，返回True
        # 时间复杂度：O(n+m)，n为节点数，m为边数
        # 空间复杂度：O(n+m)，n为节点数，m为边数
        # 邻接表
        '''
        adj = [[] for _ in range(numCourses)]
        # 初始化邻接表
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        # 记录节点的状态，0表示未访问，1表示正在访问，2表示已经访问
        visited = [0] * numCourses
        # 深度优先遍历
        def dfs(i):
            # 如果节点正在访问，说明有环
            if visited[i] == 1:
                return False
            # 如果节点已经访问过，说明没有环
            if visited[i] == 2:
                return True
            # 标记节点正在访问
            visited[i] = 1
            # 遍历节点的邻接表，进行深度优先遍历
            for j in adj[i]:
                if not dfs(j):
                    return False
            # 标记节点已经访问
            visited[i] = 2
            return True
        # 遍历每个节点
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        '''
        # BFS
        # 1. 使用邻接表存储图
        # 2. 统计每个节点的入度
        # 3. 将入度为0的节点加入队列
        # 4. 遍历队列，将队列中的节点出队，将其指向的节点的入度减1，如果入度为0，加入队列
        # 5. 如果遍历完队列后，所有节点的入度都为0，说明没有环，否则有环
        # 时间复杂度：O(n+m)，n为节点数，m为边数
        # 空间复杂度：O(n+m)，n为节点数，m为边数
        

    
# @lc code=end

