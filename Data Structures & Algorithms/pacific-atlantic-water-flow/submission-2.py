class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 當很多起點都要找同一個終點時，可以考慮從終點反向搜尋
        # starting from ocean, see what are the blocks that will be stepped on
        # use dfs to explore the route (from low -> high)
        # respectively record pac and atl, get the intersection as result

        pac = set()
        atl = set()

        m = len(heights) # row
        n = len(heights[0]) # col
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited):
            
            # mark visited
            visited.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                # stop criteria:

                if nr >= m or nr < 0 or nc >=n or nc < 0:
                    continue

                if heights[nr][nc] < heights[r][c]:
                    continue
                
                if (nr, nc) in visited:
                    continue

                # 每找到一個合法的下一格，就立刻 DFS 探索那個格子
                dfs(nr, nc, visited)

        # start from the border

        # top & down
        # top: (0, 0), (0, 1), (0, 2), (0, 3), (0, 4)
        # down: (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)

        for c in range(n): # m = 0, 1, 2, n = 0, 1, 2, 3, 4
            dfs(0, c, pac)
            dfs(m-1, c, atl)

        # left & right
        # left: (0, 0), (1, 0), (2, 0)
        # right: (0, 4), (1, 4), (2, 4)

        for r in range(m):
            dfs(r, 0, pac)
            dfs(r, n-1, atl)

        result = []

        for r, c in pac & atl:
            result.append([r, c])

        return result








