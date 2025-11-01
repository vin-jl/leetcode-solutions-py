class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        count = 0
        visited = set()

        def dfs(node):
            for neighbour in adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
        
        for i in range(n):
            if i not in visited:
                count+=1
                visited.add(i)
                dfs(i)
        
        return count    
