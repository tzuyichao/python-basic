class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        leaves = []
        g = []
        for i in range(0, n):
            g.append(set())
        for edge in edges:
            g[edge[0]].add(edge[1])
            g[edge[1]].add(edge[0])
        for i in range(0, n):
            if len(g[i]) == 1:
                leaves.append(i)
        ##print(leaves)
        while n > 2:
            n -= len(leaves)
            newleaves = []
            for leave in leaves:
                for t in g[leave]:
                    g[t].remove(leave)
                    if len(g[t]) == 1:
                        newleaves.append(t)
            leaves = newleaves
        return leaves
        
solver = Solution()
print(solver.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))