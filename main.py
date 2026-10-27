import collections
from typing import List

#Island Perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:


grid = [
    [1,1,0,0],
    [1,0,0,0],
    [1,1,1,0],
    [0,0,1,1]
]


# Output: 18
print(Solution().islandPerimeter(grid))
