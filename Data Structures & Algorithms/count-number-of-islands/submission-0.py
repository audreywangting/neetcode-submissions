class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1. build the map
        # 2. use dfs to explore the entire island, mark visited
        # 3. traverse the map, count how many island

        m = len(grid)
        n = len(grid[0])
        island = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return 
            
            # mark visited 
            grid[r][c] = "0"
            
            # explore
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r, c)

        return island



