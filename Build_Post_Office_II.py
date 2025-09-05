"""
Build Post Office II

You are given a 2D grid of integers where:

0 represents empty land (walkable),

1 represents a house (must be served),

2 represents a wall/obstacle (not walkable).

You may build exactly one post office on any empty land cell. Movement is allowed in four directions (up, down, left, right) and you may only move through empty land cells (0). You cannot pass through walls (2) or through houses (1).

The distance between two cells is defined as the length of the shortest path (number of steps) moving only through empty land cells. Your task is to minimize the sum of distances from the post office to all houses.

Return the minimum possible sum of distances. If there is no empty land from which all houses are reachable, return -1.

Input:
An n x m integer grid grid.

Output:
An integer — the minimal total distance from a chosen empty cell to all houses, or -1 if impossible.

Notes / Clarifications:

The post office must be placed on a cell with value 0.

Paths cannot go through cells with value 1 or 2.

If there are no houses or no empty cells, treat the result as impossible for this variant (return -1) unless your platform specifies otherwise.

grid =
[
  [0, 1, 0],
  [0, 0, 0],
  [0, 1, 0]
]
Output: 4
Explanation: Place the post office at the center (1,1). Shortest-path distances to the two houses are 1 and 1; sum = 1.

"""
from collections import deque
from sys import maxsize

class Solution:
    def shortestDistance(self, grid):
        
        if not grid or not grid[0]:
            return -1
        
        n = len(grid)
        m = len(grid[0])

        # dist = [[maxsize] * m for i in range(n)]
        dist = [[0] * m for i in range(n)]
        reachable_count = [[0] * m for j in range(n)]
        min_dist = maxsize
        
        buildings = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, n, m, reachable_count)
                    buildings += 1
        
        for i in range(n):
            for j in range(m):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        
        return min_dist if min_dist != maxsize else -1
    
    def bfs(self, grid, i, j, dist, n, m, reachable_count):
        visited = [[False] * m for x in range(n)]
        visited[i][j] = True
        queue = deque([(i, j, 0)])
        
        while queue:
            i, j, k = queue.popleft()
            
            # if dist[i][j] == maxsize:
            #     dist[i][j] = 0
            
            dist[i][j] += k
            
            for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + i, y + j
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    
                    # only 0 could pass
                    if grid[nx][ny] == 0:
                        queue.append((nx, ny, k + 1))
                        reachable_count[nx][ny] += 1

if __name__ == '__main__':
    sol = Solution()
    grid = [[0,1,0,0,0],
            [1,0,0,2,1],
            [0,1,0,0,0]]
    result = sol.shortestDistance(grid)
    print(result)      

