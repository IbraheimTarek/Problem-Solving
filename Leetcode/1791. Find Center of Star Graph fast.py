from typing import List
#O(1) solution
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # just check the first two edges in the list. The node common to both is our center.
        # This works because, in a star graph with N-1 edges, only the center node has a degree greater than 1.
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
    
solve = Solution()
edges = [[1,2],[2,3],[4,2]]
print(solve.findCenter(edges))