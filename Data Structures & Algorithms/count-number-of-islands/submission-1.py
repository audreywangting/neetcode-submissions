class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use dfs to explore the island area
        # when there's no connected island, # of island + 1

        m = len(grid) # row
        n = len(grid[0]) # col
        island = 0

        # 2. dfs helper
        def dfs(r, c):
            
            # base case
            if r >= m or r < 0 or c >= n or c < 0 or grid[r][c] == "0":
                return 

            # mark visited
            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # 3. traverse the grid
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r, c)

        return island



