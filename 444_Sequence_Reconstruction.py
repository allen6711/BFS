from collections import defaultdict, deque

class Solution:
    def sequenceReconstruction(self, nums: list[int], sequences: list[list[int]]) -> bool:
        graph = self.build_graph(sequences)
        topo_order = self.topological_sort(graph)
        
        return topo_order == nums

    def build_graph(self, sequences):
        # initialize graph
        graph = defaultdict(list)
        
        # It's wrong, because the length of seq may be bigger than 2
        # for u, v in sequences:
        #     graph[u].add(v)
        
        for seq in sequences:
            for node in seq:
                graph[node] = set()
        
        for seq in sequences:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])
        
        return graph

    def get_indegree(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        
        return indegrees
    
    def topological_sort(self, graph):
        indegrees = self.get_indegree(graph)
        
        # queue = []
        # for node in graph:
        #     if indegrees[node] == 0:
        #         queue.append(node)
        
        queue = [node for node in graph if indegrees[node] == 0]
        topo_order = []
        
        while queue:
            if len(queue) > 1:
                # there must exist more than one topo orders
                return None
            
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topo_order) == len(graph):
            return topo_order

        return None
    
if __name__ == '__main__':
    sol = Solution()
    result = sol.sequenceReconstruction([1,2,3], [[1,2],[1,3]])
    print(result)
    result = sol.sequenceReconstruction([1,2,3], [[1,2]])
    print(result)
    result = sol.sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]])
    print(result)
    result = sol.sequenceReconstruction([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]])
    print(result)