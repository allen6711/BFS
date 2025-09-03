from collections import defaultdict, deque

class Solution:
    def countComponents(self, n, edges: list[list[int]]) -> int:
        
        neighbors = defaultdict(list)
        
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        visited = set()
        components = 0
        
        for start in range(n):
            if start in visited:
                continue
            
            queue = deque([start])
            visited.add(start)
            components += 1
            
            while queue:
                cur = queue.popleft()
                visited.add(cur)
                
                for neighbor in neighbors[cur]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return components
    
if __name__ == '__main__':
    sol = Solution()
    result = sol.countComponents(5, [[0,1],[1,2],[3,4]])
    print(result)
    result = sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]])
    print(result)

""" 
U — Understand

We're given n nodes labeled 0..n-1 and an undirected edge list. The task is to return the number of connected components in the graph.

M — Match

This is a standard connectivity problem. Two common approaches fit well:

BFS/DFS flood fill to count components.

Union-Find (DSU) to union endpoints and count sets.
I'll use BFS here to align with the code.

P — Plan

“Plan with BFS:

Build an adjacency list for an undirected graph (add both directions).

Maintain a visited set.

Loop start from 0 to n-1.

If start is not visited, that indicates a new component: increment the answer and run BFS from start.

BFS details:

Initialize a queue with start and mark it visited.

While the queue is not empty: pop a node u; for each neighbor v, if not visited, mark visited and enqueue.

After scanning all nodes, the component counter is the result.

P — Possible Pitfalls

“Marking visited at the wrong time: mark on enqueue to avoid enqueuing the same node multiple times from different parents.”

“Forgetting bidirectional edges in the adjacency list for an undirected graph.”

“Isolated nodes: make sure the outer loop for start in range(n) detects them as single-node components.”

“Using the heavy queue.Queue in single-threaded BFS; prefer collections.deque for speed.”

“If switching to recursive DFS, watch out for recursion depth on large graphs.”

R — Review / Test

“n=5, edges=[[0,1],[1,2],[3,4]] → components = 2.”

“n=5, edges=[[0,1],[1,2],[2,3],[3,4]] → components = 1.”

“n=4, edges=[] → components = 4 (all isolated).”

“Triangle 0-1-2-0 plus isolated 3: n=4, edges=[[0,1],[1,2],[2,0]] → components = 2.”

E — Evaluate (Complexity)

“Time: O(n + m) to build adjacency and run BFS across all nodes (m = len(edges)).

Space: O(n + m) for adjacency, visited set, and the queue.”
"""