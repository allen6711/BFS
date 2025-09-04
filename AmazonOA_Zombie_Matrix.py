
class Solution:
    def zombie(self, grid):
        
        n = len(grid)
        if n == 0:
            return 0
        
        m = len(grid[0])
        if m == 0:
             return 0
         
        queue = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append((i, j))
        
        d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        days = 0
        
        while queue:
            days += 1
            new_queue = []
            
            # still run when all human were infected
            for node in queue:
                for k in range(4):
                    x = node[0] + d[k][0]
                    y = node[1] + d[k][1]
                    
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 0:
                        grid[x][y] = 1
                        new_queue.append((x, y))
            
            queue = new_queue
        
        # cannot infect all humans
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    return -1
        
        return days - 1
    
if __name__ == '__main__':
    sol = Solution()
    matrix = [
              [0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0],
              [0, 0, 0, 0, 1],
              [0, 1, 0, 0, 0]
             ]

    result = sol.zombie(matrix)
    print(result)
    matrix = [[0,1,2,0,0],
              [1,0,0,2,1],
              [0,1,0,0,0]]

    result = sol.zombie(matrix)
    print(result)
    matrix = [[0,0,0],
              [0,0,0],
              [0,0,1]]

    result = sol.zombie(matrix)
    print(result)