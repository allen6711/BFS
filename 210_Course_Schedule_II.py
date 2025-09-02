from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # BFS
        n = numCourses
        node_indegree = {x: 0 for x in range(n)}
        node_neighbors = {x: [] for x in range(n)}
        
        for to_node, from_node in prerequisites:
            node_indegree[to_node] += 1
            node_neighbors[from_node].append(to_node)
            
        start_nodes = [node for node in range(n) if node_indegree[node] == 0]
        queue = deque(start_nodes)
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in node_neighbors[node]:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == numCourses else []


if __name__ == '__main__':
    sol = Solution()
    result = sol.findOrder(2, [[1, 0]])
    print(result)
    result = sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print(result)