from typing import List
#O(N) solution
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = {} # unordered hashmap
        for edge in edges:
            # for each edge, increment the degree of nodes this edge connects in the map
            degree[edge[0]] = degree.get(edge[0],0) + 1
            degree[edge[1]] = degree.get(edge[1],0) + 1
            # If edge[1] is not found in the dictionary, get will return the default value, which is 0 in this case.
        for node, count in degree.items():
            if count == len(edges):
                return node
        return -1
    
solve = Solution()
edges = [[1,2],[2,3],[4,2]]
print(solve.findCenter(edges))