from collections import deque

class Solution:
    def orangeRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        minutes = 0
        fresh = 0
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                
                if grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        direct = ((0, 1), (1, 0), (0, -1), (-1, 0))

        while queue:
            minutes += 1
            
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in direct:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
        
        return minutes - 1 if fresh == 0 else -1


if __name__ == '__main__':
    sol = Solution()
    grid = [[2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]]
    result = sol.orangeRotting(grid)
    print(result)   # 4
    grid = [[2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]]
    result = sol.orangeRotting(grid)
    print(result)   # -1
    grid = [[0, 2]]
    result = sol.orangeRotting(grid)
    print(result)   # 0
    grid = [[0]]
    result = sol.orangeRotting(grid)
    print(result)   # 0