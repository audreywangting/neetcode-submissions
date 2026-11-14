class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # flowing from low to high
        # initialize 2 sets as pac and atl
        # dfs to explore water to pac & atl seperately
        # get the union of the pac and atl

        m = len(heights)
        n = len(heights[0])

        pac = set()
        atl = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # up, down right, left

        def dfs(r, c, visited):
            # 從海洋出發，搜尋並收集所有符合條件、能把水流回該海洋的格子
            visited.add((r, c))

            # explore diff directions
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc


                # check boundary
                if nr >= m or nr < 0 or nc >= n or nc < 0:
                    continue

                # if visited
                if (nr, nc) in visited:
                    continue

                # if the next step is not >= current level
                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, visited)

        # start exploring from ocean
        for r in range(m):
            # left & right for pac & atl
            dfs(r, 0, pac)
            dfs(r, n-1, atl)

        for c in range(n):
            # top & bottom for pac & atl
            dfs(0, c, pac)
            dfs(m-1, c, atl)

        result = []
        for r, c in pac & atl:
            result.append([r, c])
        
        return result

