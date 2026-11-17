from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # directed, no cycle => topological sort, use bfs + indegree
        # graph: quickly know course dependencies with O(1)
        # indegree: know how many prerequisite left to take 
        # queue: what classes to take next

        indegree = [0] * numCourses
        graph = defaultdict(list)
        q = deque()
        completed = 0

        # 1. build indegree & graph
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # 2. initialize q with courses' whose indegree = 0
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)            

        # 3. bfs
        while q:
            course = q.popleft()
            completed += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return completed == numCourses


            

