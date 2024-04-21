class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 建立有向圖的鄰接表和入度列表
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        
        # 深度優先搜索
        def dfs(node):
            # 如果節點已被訪問過，返回 True
            if visited[node] == 1:
                return True
            # 如果節點正在訪問中，表示存在環，返回 False
            if visited[node] == -1:
                return False
            
            # 將節點標記為訪問中
            visited[node] = -1
            
            # 對節點的所有後繼節點進行深度優先搜索
            for successor in graph[node]:
                if not dfs(successor):
                    return False
            
            # 將節點標記為已訪問
            visited[node] = 1
            return True
        
        # 初始化節點訪問狀態列表
        visited = [0] * numCourses
        
        # 對每個節點進行深度優先搜索
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
