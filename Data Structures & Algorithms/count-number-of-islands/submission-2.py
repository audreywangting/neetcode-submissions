class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use dfs to keep searching the area of one island
        # use for loop to keep finding new island
            # maintain "visited" to prevent from searching twice
        visited = set()
        n = len(grid) # row
        m = len(grid[0]) # col
        count = 0
        # 1. dfs to explore the island

        def dfs(r, c):
            if (0 > r or r >= n or 0 > c or c >= m or grid[r][c] == "0" or (r, c) in visited):
                return

            visited.add((r, c))
            
            # explore the island legally
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for x in range(n):
            for y in range(m):
                if grid[x][y] == "1" and (x, y) not in visited:
                    count += 1
                    dfs(x, y)

        return count 



