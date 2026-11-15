from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # use bfs to record & explore the shortest path in unweighted grid
        # first in first out, to explore near boxes
        n = len(grid)

        # check the start & end
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # build 8 directions
        directions = [(1, 0), (-1, 0), 
                    (1, 1), (-1, -1), 
                    (0, 1), (0, -1), 
                    (1, -1), (-1, 1)]

        # initialize bfs
        q = deque([(0, 0, 1)]) # row, col, distance
        visited = {(0, 0)}

        # bfs
        while q:
            r, c, dist = q.popleft()

            # if reached the end
            if r == n-1 and c == n-1:
                return dist

            # explore 8 neighbors
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <=nr < n and 0 <= nc < n
                    and grid[nr][nc] == 0 and 
                    (nr, nc) not in visited):
                    visited.add((nr, nc))
                    q.append((nr, nc, dist+1))


        return -1










