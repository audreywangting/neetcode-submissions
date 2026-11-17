from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph: 快速找尋依賴關係，記錄每堂課完成之後會影響什麼課
        # indegree: 記錄每堂課有哪些先修還沒完成
        # queue: 紀錄目前可以修的課

        # 1. build graph & prerequisite
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # 2. initialize queue w/ indegree = 0
        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        # 3. BFS
        completed = 0 # record num of course completed

        while q:
            course = q.popleft()
            completed += 1

            # 每完成一門課。就把依賴他的課程 indegree -= 1
            # graph = {0:[1, 2], 1:[3], 2:[3]}
            for neighbor in graph[course]: # 找出依賴course的課程
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return completed == numCourses







