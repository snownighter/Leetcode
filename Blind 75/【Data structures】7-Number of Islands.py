class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        if not grid:
            return 0
        
        # 定義方向
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        rows, cols = len(grid), len(grid[0])
        
        def dfs(row, col):

            grid[row][col] = '0'
            # 標記與當前位置相鄰的 '1' 為 '0'
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '1':
                    dfs(new_row, new_col)
        
        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)
        
        return island_count
