from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        n = numCourses
        node_indegree = {x: 0 for x in range(n)}
        node_neighbor = {x: [] for x in range(n)}
        
        for to_node, from_node in prerequisites:
            node_indegree[to_node] += 1
            node_neighbor[from_node].append(to_node)
        
        start_nodes = [node for node in range(n) if node_indegree[node] == 0]
        queue = deque(start_nodes)
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in node_neighbor[node]:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(result) == numCourses

if __name__ == '__main__':
    sol = Solution()
    result = sol.canFinish(2, [[1, 0]])
    print(result)
    result = sol.canFinish(2, [[1, 0], [0, 1]])
    print(result)