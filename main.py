import collections
from typing import List

#Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:



image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2

# Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
print(Solution().floodFill(image,sr,sc,color))
