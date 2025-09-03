from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # number of edges should be same as n - 1
        # else: circle
        if len(edges) != n - 1:
            return False
        
        neighbors = defaultdict(list)
        
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        visited = {}
        
        queue = deque([0])
        visited[0] = True
        
        while queue:
            cur = queue.popleft()
            # visited[cur] = True
            
            for node in neighbors[cur]:
                if node not in visited:
                    visited[node] = True   # mark as visited before enqueuing
                    queue.append(node)
        
        return len(visited) == n

if __name__ == '__main__':
    sol = Solution()
    result = sol.validTree(5, [[0,1],[0,2],[0,3],[1,4]])
    print(result)
    result = sol.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])
    print(result)
    

"""_
U — Understand

Input: n nodes labeled 0..n-1, and an undirected edge list edges.

Goal: Determine if the graph forms a valid tree.

Tree (undirected) criteria: The graph must be connected and acyclic.

Equivalent condition: An undirected graph is a tree iff it has exactly n - 1 edges and is connected.

M — Match

Use the tree characterization:

Edge-count check: len(edges) == n - 1.

Connectivity check: BFS/DFS from any node (e.g., 0) visits all n nodes.

Alternative: Union-Find to detect a cycle and ensure connectivity with the same edge-count check.

P — Plan

If len(edges) != n - 1, return False immediately.

Build an adjacency list for the undirected graph (add both directions).

Run BFS (or DFS) from node 0, count visited nodes.

Return True iff visited count equals n.

I — Implement (BFS)

P — Possible Pitfalls

Forgetting the edge-count filter (you might accept cyclic graphs if only checking connectivity).

Building only one direction for undirected edges (must add both u->v and v->u).

Isolated nodes: BFS won’t reach them ⇒ not connected.

Python 3 module names: use collections.deque (not Queue), from queue import Queue only for multithreading.

R — Review / Test

Connected tree: n=5, edges=[[0,1],[0,2],[0,3],[1,4]] → True.

Cycle: n=5, edges=[[0,1],[1,2],[2,3],[1,3],[1,4]] → edge-count=5≠4 → False.

Disconnected: n=4, edges=[[0,1],[2,3],[1,2]] (3 edges but two components) → BFS visits < n → False.

Single node: n=1, edges=[] → True.

E — Evaluate (Complexity)

Time: O(n + m) to build and BFS, where m = len(edges).

Space: O(n + m) for adjacency list, queue, and visited set.
"""